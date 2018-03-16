# SDC Responses Dashboard API

## Setup
It is preferable to use the version of Python locally that matches that
used on deployment. This project has a `.python_version` file for this
purpose.


Upgrade pip and install dependencies:

```
brew install pyenv
pyenv install
pip install --upgrade pip setuptools pipenv
pipenv install
pipenv install --dev
```

Run the server inside the virtual env created by Pipenv with:

```
pipenv run ./scripts/run_app.sh

```
