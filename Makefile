start:
	pipenv run python run.py

build:
	pipenv install --dev

lint:
	pipenv run flake8 ./app
	pipenv run pylint --output-format=colorized -j 0 --reports=n ./app
