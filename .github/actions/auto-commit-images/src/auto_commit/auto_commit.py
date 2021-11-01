import base64
import os

from git import Repo
from github import Github

from auto_commit.librarian import LibraryFilename, filter_media_library_files, filter_base_images


class FileNotFoundInRepoException(Exception):
    """Raised when we try to get the sha of a non-existing file file"""
    pass


def print_repo_dir(repo_dir):
    print("repo: ", repo_dir)


def print_git_diff(repo):
    # https://git-scm.com/docs/git-diff#Documentation/git-diff.txt---diff-filterACDMRTUXB82308203

    for diff_added in repo.index.diff(None).iter_change_type('A'):
        print("Added:     ", diff_added.a_path)

    for diff_copied in repo.index.diff(None).iter_change_type('C'):
        print("Copied     ", diff_copied.a_path)

    for diff_deleted in repo.index.diff(None).iter_change_type('D'):
        print("Deleted:   ", diff_deleted.a_path)

    for diff_renamed in repo.index.diff(None).iter_change_type('R'):
        print("Renamed:   ", diff_renamed.a_path)

    for diff_modified in repo.index.diff(None).iter_change_type('M'):
        print("Modified:  ", diff_modified.a_path)

    for diff_changed in repo.index.diff(None).iter_change_type('T'):
        print("Changed:   ", diff_changed.a_path)


def print_git_untracked(repo):
    for untracked in repo.untracked_files:
        print("Untracked: ", untracked)


def print_debug_info(repo_dir, repo):
    print_repo_dir(repo_dir)
    print_git_untracked(repo)
    print_git_diff(repo)


def get_all_modified_files(repo):
    all_modified_files = []
    for diff_modified in repo.index.diff(None).iter_change_type('M'):
        all_modified_files.append(diff_modified.a_path)
    return all_modified_files


def get_new_base_images(repo):
    all_untracked_files = repo.untracked_files
    return filter_base_images(filter_media_library_files(all_untracked_files))


def get_modified_base_images(repo):
    all_modified_files = get_all_modified_files(repo)
    return filter_base_images(filter_media_library_files(all_modified_files))


def add_new_base_images_to_the_repo(repository, repo_dir, repo_token, base_image_paths, branch):
    # https://docs.github.com/en/rest/reference/repos#create-or-update-file-contents
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.create_file

    gh = Github(repo_token)

    remote_repo = gh.get_repo(repository)

    commits = []

    for base_image_path in base_image_paths:
        # Commit message
        commit_message = f'Add file {base_image_path}'
        print(commit_message)

        # File content
        image_data_binary = open(f'{repo_dir}/{base_image_path}', "rb").read()
        content = base64.b64encode(image_data_binary)

        response = remote_repo.create_file(
            base_image_path, commit_message, content, branch)

        commits.append(response['commit'].sha)

    return commits


def get_previous_file_sha(remote_repo, file_path, branch):
    # GitHub API does not allow to download files bigger than 1MB and there is not any API endpoint to get the current sha of a file.
    # The simplest solution is to get the sha from a get_contents endpoint using a directory. The endpoint returns the sha of the file.
    # for every file in the direectory.
    dirname = os.path.dirname(file_path)

    dir_content = remote_repo.get_contents(dirname, branch)

    for file in dir_content:
        if (file.path == file_path):
            return file.sha

    raise FileNotFoundInRepoException(
        f'Error: trying to get sha for missing file {file_path} in branch {branch}')


def update_base_images_in_the_repo(local_repo, repository, repo_dir, repo_token, base_image_paths, branch):
    # https://docs.github.com/en/rest/reference/repos#create-or-update-file-contents
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.update_file

    gh = Github(repo_token)

    remote_repo = gh.get_repo(repository)

    commits = []

    for base_image_path in base_image_paths:
        # Commit message
        commit_message = f'Update file {base_image_path}'
        print(commit_message)

        file_path = f'{repo_dir}/{base_image_path}'

        # File content
        image_data_binary = open(file_path, "rb").read()
        base_64_content = base64.encodebytes(image_data_binary)

        sha = get_previous_file_sha(remote_repo, base_image_path, branch)

        response = remote_repo.update_file(
            base_image_path, commit_message, base_64_content, sha, branch)

        commits.append(response['commit'].sha)

    return commits


def auto_commit(repository, repo_dir, repo_token, branch):
    local_repo = Repo(repo_dir)

    print_debug_info(repo_dir, local_repo)

    # New Base images
    new_base_image_paths = get_new_base_images(local_repo)
    print("New Base images: ", new_base_image_paths)
    commits_new_images = add_new_base_images_to_the_repo(
        repository, repo_dir, repo_token, new_base_image_paths, branch)

    # Modified Base images
    modifed_base_image_paths = get_modified_base_images(local_repo)
    print("Modified Base images: ", modifed_base_image_paths)
    commits_for_updates = update_base_images_in_the_repo(
        local_repo, repository, repo_dir, repo_token, modifed_base_image_paths, branch)

    return commits_new_images + commits_for_updates
