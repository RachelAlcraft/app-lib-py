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
Follow these instructions for creating a token in pypi and adding it to the github repo: https://www.seanh.cc/2022/05/21/publishing-python-packages-from-github-actions/
https://github.com/marketplace/actions/modify-file-content

### 7b. Streamlit

### 7c. Docker
