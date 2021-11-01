# Auto-commit Base images

Base images are in the folder `public/images/`. They are copied from the `library\data` folder. This action detects newly added or updated images and generates a signed commit to add them to the repository.

The corresponding command is you want to do it manually is:

```
git add public/images/000001-42.600.2.tif
git commit -S -m "Add new image 000001-42.600.2.tif"
git push
```

or

```
git add public/images/000001-42.600.2.tif
git commit -S -m "Update image 000001-42.600.2.tif"
git push
```

Commits are added using GitHub API: https://gist.github.com/swinton/03e84635b45c78353b1f71e41007fc7c

## Usage

You need to add the action in your workflow:

```yaml
- name: Auto-commit
  uses: ./.github/actions/auto-commit
```

### Outputs

| Input              | Description                       |
|--------------------|-----------------------------------|
| `repo_dir`         | Dir with the Git repo             |
| `changes_detected` | True if files have been committed |

### Development

> IMPORTANT: this sample commands have to be executed from `.github/actions/auto-commit-images` folder.

> You can use [act](https://github.com/nektos/act) to run the action locally within a workflow.

Build docker image:
```
docker build --no-cache -t act-github-actions-auto-commit-images:latest .
```

Run GitHub action locally with docker:
```
docker run --rm -it \
  --env INPUT_REPOSITORY=Nautilus-Cyberneering/chinese-ideographs-website \
  --env INPUT_REPO_DIR=/repo \
  --env INPUT_REPO_TOKEN=XXX \
  --env INPUT_BRANCH=main \
  --volume $(pwd)/src:/app \
  --volume $(pwd)/../../..:/repo \
  act-github-actions-auto-commit-images
```

Check linting for `Dockerfile`:
```
docker run --rm -i hadolint/hadolint < ./Dockerfile
```

### Testing

Build docker image:
```
docker build --target testing --no-cache -t  act-github-actions-auto-commit-images-test .
```

Run tests:
```
docker run --rm \
  --volume $(pwd)/src:/app \
  act-github-actions-auto-commit-images-test pytest
```
