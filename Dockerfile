FROM node:11.7-alpine AS yarn-compile
WORKDIR /app
COPY . /app
EXPOSE 8078
COPY package*.json ./
COPY yarn.lock ./
RUN yarn compile

FROM python:3.9.1-alpine AS python-app
WORKDIR /app
COPY --from=yarn-compile /app /app
RUN pip3 install -U pipenv && pipenv install --system --deploy
ENTRYPOINT ["python3"]
CMD ["run.py"]
