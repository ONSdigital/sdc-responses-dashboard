FROM mhart/alpine-node

WORKDIR /app
COPY . /app
EXPOSE 8078

COPY package*.json ./
COPY yarn.lock ./
RUN yarn compile

FROM python:alpine3.6

WORKDIR /app
COPY --from=0 /app /app
RUN pip3 install -U pipenv && pipenv install --system --deploy

ENTRYPOINT ["python3"]
CMD ["run.py"]
