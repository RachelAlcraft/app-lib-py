# Create dev environments for both the app and the lib seperately

**Use the appropriate one for the dev work. Keep a seperation in your mind between the scientific library (lib) and the demonstration of it (app).**

# Virtual environments

## STREAMLIT APP
```
python -m venv .env-app
## Load dev environment
source .env-app/bin/activate
(deactivate to exit venv)
pip install --upgrade pip
pip install -r requirements.txt --upgrade
```
Add the env path to your .gitignore

### run app
streamlit run app/home.py

## Pypi library
```
python -m venv .env-lib
## Load dev environment
source .env-lib/bin/activate
(deactivate to exit venv)
pip install --upgrade pip
pip install -r requirements_lib.txt --upgrade
```

Add the env path to your .gitignore

## distribute to streamlit
This can be be automatically distributed to streamlit on push to main once you have set the link to do this up here [streamlit app](https://share.streamlit.io/)


# Debugging

## A python file

## The streamlit app
