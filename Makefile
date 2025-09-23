start:
#	yarn compile
	pipenv run python run.py

compile:
	yarn compile

build:
	pipenv install --dev

# remove --ignore=70624 --ignore=72731 once flask-cors updated beyond 5.0.0
# remove --ignore=70612 once jinja2 is updated beyond 3.1.4
lint:
	pipenv run isort .
	pipenv run black --line-length 120 .
	pipenv run flake8

lint-check:
	pipenv run isort --check-only .
	pipenv run black --line-length 120 --check .
	pipenv run flake8

test: lint-check
	pipenv run pytest tests --cov-report term-missing --cov app --capture no

mock_services:
	pipenv run python scripts/mock_services.py

smoke_test:
	pipenv run behave tests/functional/smoke_tests/features
