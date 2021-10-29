import os
import json

from auto_commit.auto_commit import auto_commit


def main(repo_dir):
    auto_commit(repo_dir)
    print("::set-output name=changes_detected::false")


if __name__ == "__main__":
    repo_dir = os.environ["INPUT_REPO_DIR"]
    main(repo_dir)
