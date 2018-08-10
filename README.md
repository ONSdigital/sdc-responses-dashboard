# SDC Responses Dashboard
[![Build Status](https://api.travis-ci.org/ONSdigital/sdc-responses-dashboard.svg?branch=master)](https://travis-ci.org/ONSdigital/sdc-responses-dashboard)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/80ad95f7aaa9477da6aa8fd9aec40f52)](https://www.codacy.com/project/MebinAbraham/sdc-responses-dashboard/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ONSdigital/sdc-responses-dashboard&amp;utm_campaign=Badge_Grade_Dashboard)

## Run the application

**Initial Setup:**

Install pyenv and pipenv
```bash
brew install pyenv
pyenv install
pip install --U pip setuptools pipenv
```

**Run with Make:**

Install dependencies with
```bash
make build
```

Run with
```bash
make start
```

**Alternatively, run manually:**

Install dependencies to run:
```bash
pipenv install
```

Install dependencies to develop:
```bash
pipenv install --dev
```

Run the server inside the virtual env created by Pipenv with:

```bash
pipenv run python run.py
```

## Running in Isolation
To run the dashboard without any of the external services it calls, this repo includes a basic flask app which mocks
the external services.

Bring it up with :
```bash
make mock_services
```

And set these environment variables for the dashboard app:
```.dotenv
COLLECTION_EXERCISE_URL=http://localhost:5001/
SURVEY_URL=http://localhost:5001/
REPORTING_URL=http://localhost:5001/
```

## Testing and Linting

Run linting with
```bash
make lint
```
