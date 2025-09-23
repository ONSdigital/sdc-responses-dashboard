FROM python:3.11-alpine AS python-app
WORKDIR /app
RUN pip3 install -U pipenv && pipenv install --system --deploy
ENTRYPOINT ["python3"]
CMD ["run.py"]
