start:
	pipenv run python run.py

build:
	pipenv install --dev

lint:
	pipenv run flake8 ./app
	pipenv run pylint --output-format=colorized -j 0 --reports=n ./app

check:
	pipenv check

test: check lint
	pipenv run pytest tests --cov-report term-missing --cov app --capture no

mock_services:
	pipenv run python scripts/mock_services.py
