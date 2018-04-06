# SDC Responses Dashboard API
[![Build Status](https://api.travis-ci.org/ONSdigital/sdc-responses-dashboard-api.svg?branch=master)](https://travis-ci.org/ONSdigital/sdc-responses-dashboard-api)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7aaabdc5ce3a47e587d95f6e2243be82)](https://www.codacy.com/app/MebinAbraham/sdc-responses-dashboard-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ONSdigital/sdc-responses-dashboard-api&amp;utm_campaign=Badge_Grade)

## Run the application

**Initial Setup:**

Install pyenv and pipenv
```
brew install pyenv
pyenv install
pip install --U pip setuptools pipenv
```

**Run with Make:**

Install dependencies with
```
make build
```

Run with
```
make start
```

**Alternatively, run manually:**

Install dependencies to run:
```
pipenv install
```

Install dependencies to develop:
```
pipenv install --dev
```

Run the server inside the virtual env created by Pipenv with:

```
pipenv run python run.py
```

## Testing and Linting

Run linting with
```
make lint
```
