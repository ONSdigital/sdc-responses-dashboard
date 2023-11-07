FROM node:21.7-alpine AS yarn-compile
WORKDIR /app
COPY . /app
EXPOSE 8078
COPY package*.json ./
COPY yarn.lock ./
RUN yarn compile

FROM python:3.11-alpine AS python-app
WORKDIR /app
COPY --from=yarn-compile /app /app
RUN pip3 install -U pipenv && pipenv install --system --deploy

CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "4", "--timeout", "60", "app.setup:create_app()"]
