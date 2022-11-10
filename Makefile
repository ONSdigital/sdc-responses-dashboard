start:
	yarn compile
	pipenv run python run.py

compile:
	yarn compile

build:
	pipenv install --dev

lint:
	pipenv check -i 51499
	pipenv run isort .
	pipenv run black --line-length 120 .
	pipenv run flake8

lint-check:
	pipenv check -i 51499
	pipenv run isort --check-only .
	pipenv run black --line-length 120 --check .
	pipenv run flake8

test: lint-check
	pipenv run pytest tests --cov-report term-missing --cov app --capture no

mock_services:
	pipenv run python scripts/mock_services.py

smoke_test:
	pipenv run behave tests/functional/smoke_tests/features
