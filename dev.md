# Create dev environments for both the app and the lib seperately

**Use the appropriate one for the dev work. Keep a seperation in your mind between the scientific library (lib) and the demonstration of it (app).**

# Virtual environments

## STREAMLIT APP
```
/usr/bin/python3.12 -m venv .env-app
## Load dev environment
source .env-app/bin/activate
(deactivate to exit venv)
pip install --upgrade pip
pip install -r requirements.txt --upgrade
```

### run app
streamlit run app/home.py

## distribute to streamlit
This will be automatically distributed to streamlit on push to main
https://share.streamlit.io/

## Pypi library
```
/usr/bin/python3.12 -m venv .env-lib
## Load dev environment
source .env-lib/bin/activate
(deactivate to exit venv)
pip install --upgrade pip
pip install -r requirements_lib.txt --upgrade
```

---

# Debugging

## A python file

## The streamlit app
