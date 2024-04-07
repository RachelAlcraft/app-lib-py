# app-lib-py

This template is a suggestion of good practice for a scientific python library that includes continuous integration and conntinuous development and continuous documentation.
The application is demonstrated though streamlist which is deployed with continuous deployment, and also made a available via pypi as a python library with `pip install`

The single github repo contains 2 seperate software artefacts, a python library that can be installed and used by others, and a streamlit web application that demonstreates the library and provides a simple usage. Additionally there is a docker file which allows the upload of a docker image to dockerhub for a middle use of locally hosted web application.

To use this library yourself, use the "Template" button as described below.

## 1. Create a template for yourself

## 2. Change the name (search on app-lib-py or app_lib_py)
- in the yml files in pydoctor line 24
- docker yml line 26
- pypi yml line 43

## 2. Setup development environments
See [dev environments](dev.md)

## 3. Setup precommit hooks
https://pre-commit.com/
Run it to check
`pre-commit run --all-files`
`ruff --target-version=py311 --line-length 88 . --fix`
`black ./ --check --line-length 88 --diff`

## 4. Change the tokens, get all workflows in github actions working

pydoctor --make-html --html-output=./docs/api lib/src/app_lib_py --theme readthedocs

## 5. Test driven development, design the functionality

## 6. Implement

## 7. Distribute and deploy

### 7a. Pypi
Tokens are needed from pypi and from github. Follow these instructions: [pypi gha](https://www.seanh.cc/2022/05/21/publishing-python-packages-from-github-actions/)

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
