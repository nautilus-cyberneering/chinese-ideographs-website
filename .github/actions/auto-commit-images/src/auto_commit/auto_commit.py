import base64
import os

from git import Repo
from github import Github, enable_console_debug_logging

from auto_commit.librarian import (LibraryFilename, filter_base_images,
                                   filter_media_library_files)


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


def get_all_deleted_files(repo):
    all_deleted_files = []
    for diff_deleted in repo.index.diff(None).iter_change_type('D'):
        all_deleted_files.append(diff_deleted.a_path)
    return all_deleted_files


def get_new_base_images(repo):
    all_untracked_files = repo.untracked_files
    return filter_base_images(filter_media_library_files(all_untracked_files))


def get_modified_base_images(repo):
    all_modified_files = get_all_modified_files(repo)
    return filter_base_images(filter_media_library_files(all_modified_files))


def get_deleted_base_images(repo):
    all_deleted_files = get_all_deleted_files(repo)
    return filter_base_images(filter_media_library_files(all_deleted_files))


def file_exists_in_branch_and_has_the_same_content(local_repo, remote_repo, repo_file_path, branch):
    remote_sha = file_exists_in_branch(remote_repo, repo_file_path, branch)
    local_sha = local_repo.git.hash_object(repo_file_path)

    # Debug info
    print("Checking file sha ...")
    print("Repo file path: ", repo_file_path)
    print("Remote sha: ", remote_sha)
    print("Local sha: ", local_sha)

    file_already_commited_in_branch = False
    if (local_sha == remote_sha):
        file_already_commited_in_branch = True

    return file_already_commited_in_branch


def add_new_base_images_to_the_repo(local_repo, repository, repo_dir, repo_token, repo_base_image_paths, branch):
    # https://docs.github.com/en/rest/reference/repos#create-or-update-file-contents
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.create_file

    gh = Github(repo_token)

    remote_repo = gh.get_repo(repository)

    commits = []

    for repo_base_image_path in repo_base_image_paths:

        file_path = f'{repo_dir}/{repo_base_image_path}'

        # Commit message
        commit_message = f'Add file {repo_base_image_path}'

        # Debug info
        print("Auto-commit to add image: ")
        print("File path: ", file_path)
        print("Repo dir: ", repo_dir)
        print("Repo Base image path: ", repo_base_image_path)
        print("Commit message: ", commit_message)
        print("Branch: ", branch)

        if (file_exists_in_branch_and_has_the_same_content(local_repo, remote_repo, repo_base_image_path, branch)):
            # Skip commit if the file with the same content already exist in the branch
            continue

        # File content
        image_data = open(file_path, "rb").read()

        enable_console_debug_logging()

        response = remote_repo.create_file(
            repo_base_image_path, commit_message, image_data, branch)

        commits.append(response['commit'].sha)

    return commits


def get_file_sha(remote_repo, repo_file_path, branch):
    # GitHub API does not allow to download files bigger than 1MB and there is not any API endpoint to get the current sha of a file.
    # The simplest solution is to get the sha from a get_contents endpoint using a directory. The endpoint returns the sha of the file.
    # for every file in the direectory.
    dirname = os.path.dirname(repo_file_path)

    dir_content = remote_repo.get_contents(dirname, branch)

    for file in dir_content:
        if (file.path == repo_file_path):
            return file.sha

    raise FileNotFoundInRepoException(
        f'Error: trying to get sha for missing file {repo_file_path} in branch {branch}')


def file_exists_in_branch(remote_repo, repo_file_path, branch):
    dirname = os.path.dirname(repo_file_path)

    dir_content = remote_repo.get_contents(dirname, branch)

    for file in dir_content:
        if (file.path == repo_file_path):
            return file.sha

    return None


def update_base_images_in_the_repo(local_repo, repository, repo_dir, repo_token, repo_base_image_paths, branch):
    # https://docs.github.com/en/rest/reference/repos#create-or-update-file-contents
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.update_file

    gh = Github(repo_token)

    remote_repo = gh.get_repo(repository)

    commits = []

    for repo_base_image_path in repo_base_image_paths:
        # Commit message
        commit_message = f'Update file {repo_base_image_path}'

        file_path = f'{repo_dir}/{repo_base_image_path}'

        # File content
        image_data = open(file_path, "rb").read()

        # Previous sha for the file
        sha = get_file_sha(remote_repo, repo_base_image_path, branch)

        # Debug info
        print("Auto-commit to update image: ")
        print("File path: ", file_path)
        print("Repo dir: ", repo_dir)
        print("Repo Base image path: ", repo_base_image_path)
        print("Commit message: ", commit_message)
        print("Previous file sha: ", sha)
        print("Branch: ", branch)

        # Upload new file version
        response = remote_repo.update_file(
            repo_base_image_path, commit_message, image_data, sha, branch)

        commits.append(response['commit'].sha)

        print("Commt sha: ", response['commit'].sha)

    return commits


def delete_base_images_from_the_repo(local_repo, repository, repo_dir, repo_token, repo_base_image_paths, branch):
    # https://docs.github.com/en/rest/reference/repos#delete-a-file
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.delete_file

    gh = Github(repo_token)

    remote_repo = gh.get_repo(repository)

    commits = []

    for repo_base_image_path in repo_base_image_paths:
        # Commit message
        commit_message = f'Delete file {repo_base_image_path}'

        file_path = f'{repo_dir}/{repo_base_image_path}'

        # Previous sha for the file
        sha = get_file_sha(remote_repo, repo_base_image_path, branch)

        # Debug info
        print("Auto-commit to delete image: ")
        print("File path: ", file_path)
        print("Repo dir: ", repo_dir)
        print("Repo Base image path: ", repo_base_image_path)
        print("Commit message: ", commit_message)
        print("Previous file sha: ", sha)
        print("Branch: ", branch)

        # Upload new file version
        response = remote_repo.delete_file(
            repo_base_image_path, commit_message, sha, branch)

        commits.append(response['commit'].sha)

        print("Commt sha: ", response['commit'].sha)

    return commits


def auto_commit(repository, repo_dir, repo_token, branch):
    local_repo = Repo(repo_dir)

    print_debug_info(repo_dir, local_repo)

    # New Base images
    added_repo_base_image_paths = get_new_base_images(local_repo)
    print("Added Base images: ", added_repo_base_image_paths)
    commits_for_added_images = add_new_base_images_to_the_repo(
        local_repo, repository, repo_dir, repo_token, added_repo_base_image_paths, branch)

    # Modified Base images
    modified_repo_base_image_paths = get_modified_base_images(local_repo)
    print("Modified Base images: ", modified_repo_base_image_paths)
    commits_for_updated_images = update_base_images_in_the_repo(
        local_repo, repository, repo_dir, repo_token, modified_repo_base_image_paths, branch)

    # Deleted Base images
    deleted_repo_base_image_paths = get_deleted_base_images(local_repo)
    print("Deleted Base images: ", deleted_repo_base_image_paths)
    commits_for_deleted_images = delete_base_images_from_the_repo(
        local_repo, repository, repo_dir, repo_token, deleted_repo_base_image_paths, branch)

    return commits_for_added_images + commits_for_updated_images + commits_for_deleted_images
