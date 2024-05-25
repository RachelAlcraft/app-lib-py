# app-lib-py

Hosted at: [streamlit:app-lib-py](https://app-lib-py.streamlit.app/)

This template is a suggestion of good practice for a scientific python library that includes continuous integration and conntinuous development and continuous documentation.
The application is demonstrated though streamlist which is deployed with continuous deployment, and also made a available via pypi as a python library with `pip install`

The single github repo contains 2 seperate software artefacts, a python library that can be installed and used by others, and a streamlit web application that demonstreates the library and provides a simple usage. Additionally there is a docker file which allows the upload of a docker image to dockerhub for a middle use of locally hosted web application.

To use this library yourself, use the "Template" button as described below.

## 1. Create a template for yourself
The template can be downloaded from github at [app-lib-py](https://github.com/RachelAlcraft/app-lib-py). Once using the template and giving your own name and repo, you will need to make some changes to the files.

## 2. Change the default name
Primarily do this by searching on app-lib-py and app_lib_py, don't forget there is a directory to change too. Examples of changes are:
- in the yml files (/.github/workflows/) in pydoctor line 24
- docker yml line 26
- pypi's publish.yml line 43

## 2. Setup development environments
See [dev environments](dev.md)

## 3. Setup precommit hooks
https://pre-commit.com/
Run it to check
`pre-commit run --all-files`
`ruff --target-version=py311 --line-length 88 . --fix`
`black ./ --check --line-length 88 --diff`

## 4. PyDoctor automatic documentaion

The documentation is generated with the workflow pydoctor.yml.
The branch gh-pages will be created after your first commit to main, and will fail the first time.


The branch gh-pages will be created after your first commit to main, and will fail the first time, so re-run the action
from github actions on your github after you have done your first commit.

The pydoctor command does not need to be run locally (installing if you want to, and add the created files to .gitignore:
```pydoctor --make-html --html-output=./docs/api lib/src/app_lib_py --theme readthedocs```
Permissions need to be added so that the action has the appropriate permissions to be run.
In repo/settings/Actions at the bottom give Read and Write permissions to Workflow and Allow github to create and approve pull requests.

Then re-run the failed action.  This should create the branch gh-actions.

Now in order to activate it you must go to your github settings/pages and choose deply from a branch, and then gh-pages and root. An action will be triggered automatically to build the pages, with the link at: https://rachelalcraft.github.io/your-repo/

For pydoctor, you need the setting Actions/General/Allow GitHib Actions to create and approve pull requests checked.  Turn on gh-pages in the settings to be published from the branch gh-pages.

## 5. Test driven development, design the functionality
Write the tests in **science**, **speed** and **utility** before you write the functional implementation.

## 6. Implement
The src/app_lib_py directory is the place to write the functional code for the library. This will become available on pypi as a `pip install`.

## 7. Distribute and deploy
The github actions automate the distribtion to pypi, test running, and docker.
If you choose to distribute on streamlit this will be automated by checkin to main.

### 7a. Pypi
Tokens are needed from pypi and from github. You create a token in pypi, and then add it in github/secrets and variables/Actions with the name PYPI_API_TOKEN. Follow these instructions: [pypi gha token](https://www.seanh.cc/2022/05/21/publishing-python-packages-from-github-actions/#create-a-pypi-api-token)

You will need to create a 0.01 or some such release to get the workflow going and test it.
To release to pypi you need to either:
- Create a release in github, the tag will be the version number of the library
- Or if it is only a minor incremebt, you can run the workflow in Actions [Create a new patch release](https://github.com/RachelAlcraft/app-lib-py/actions/workflows/release.yml). This will increment the minor version and release.


### 7b. Streamlit
Streamlit will be automatically deployed when the main branch is updated after the link with streamlit is made.
1. Create an account with [streamlit io](https://streamlit.io/)
2. Go to the [deploy](https://share.streamlit.io/deploy)
3. Choose your repo: RachelAlcraft/app-lib-py
4. Choose Branch: Main
5. Choose entry file: app/home.py
6. Amend the domain to your liking [app-lib-py](https://app-lib-py.streamlit.app/)
7. Press deploy

### 7c. Docker
The application can also be added to docker for self hosting. API tokens need to be added.
1. First create an api token in docker/My Account/Security/Access Tokens
2. In github/Settings/Secrets and Variables/Actions
  - add the copied token as a secret with the name DOCKERHUB_TOKEN
  - add your docker user name with the name DOCKERHUB_USERNAME
