# SDC Responses Dashboard API

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
