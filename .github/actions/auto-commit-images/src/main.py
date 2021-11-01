import os
import json

from auto_commit.auto_commit import auto_commit


def main(repository, repo_dir, repo_token, branch):
    auto_commit(repository, repo_dir, repo_token, branch)

    # TODO
    print("::set-output name=changes_detected::false")


if __name__ == "__main__":
    repository = os.environ["INPUT_REPOSITORY"]
    repo_dir = os.environ["INPUT_REPO_DIR"]
    repo_token = os.environ["INPUT_REPO_TOKEN"]
    branch = os.environ["INPUT_BRANCH"]
    main(repository, repo_dir, repo_token, branch)
