# SDC Responses Dashboard API


## Pre-Requisites
In order to run locally you'll need PostgreSQL and Node.js installed


npm
```
brew install npm
```

Note that npm currently requires Python 2.x for some of the setup steps,
it doesn't work with Python 3.

## Setup
It is preferable to use the version of Python locally that matches that
used on deployment. This project has a `.python_version` file for this
purpose.


Upgrade pip and install dependencies:

```
brew install pyenv
pyenv install
pip install --upgrade pip setuptools pipenv
pipenv install --dev
```

Run the server inside the virtual env created by Pipenv with:

```
pipenv run ./scripts/run_app.sh

```
