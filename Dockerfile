FROM node:8.15.0-alpine

WORKDIR /app
COPY . /app
EXPOSE 8078

COPY package*.json ./
COPY yarn.lock ./
RUN yarn compile

FROM python:3.6.8-alpine

WORKDIR /app
COPY --from=0 /app /app
RUN pip3 install -U pipenv==2018.11.26 && pipenv install --system --deploy

ENTRYPOINT ["python3"]
CMD ["run.py"]
