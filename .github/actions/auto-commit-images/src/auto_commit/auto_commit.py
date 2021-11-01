import base64
import os

from git import Repo
from github import Github

from auto_commit.library_filename import LibraryFilename


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


def filter_media_library_files(filepaths):
    images = list(filter(lambda filepath: LibraryFilename.validate(
        os.path.basename(filepath)), filepaths))
    return images


def filter_base_images(filepaths):
    base_images = list(filter(lambda filepath: LibraryFilename(
        os.path.basename(filepath)).is_base_image(), filepaths))
    return base_images


def filter_untracked_base_images(untracked):
    media_library_files = filter_media_library_files(untracked)
    base_images = filter_base_images(media_library_files)
    return base_images


def get_new_base_images(repo_dir):
    repo = Repo(repo_dir)
    print_debug_info(repo_dir, repo)
    base_image_paths = filter_untracked_base_images(repo.untracked_files)
    return base_image_paths


def add_new_base_images_to_the_repo(repository, repo_dir, repo_token, base_image_paths, branch):
    # https://docs.github.com/en/rest/reference/repos#create-or-update-file-contents
    # https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository.create_file

    gh = Github(repo_token)

    repo = gh.get_repo(repository)

    for base_image_path in base_image_paths:
        # commit message
        commit_message = f'Add file {base_image_path}'
        print(commit_message)

        # file content
        image_data_binary = open(f'{repo_dir}/{base_image_path}', "rb").read()
        content = base64.b64encode(image_data_binary)

        repo.create_file(base_image_path, commit_message, content, branch)


def auto_commit(repository, repo_dir, repo_token, branch):
    base_image_paths = get_new_base_images(repo_dir)
    print("Untracked Base images: ", base_image_paths)

    add_new_base_images_to_the_repo(
        repository, repo_dir, repo_token, base_image_paths, branch)
