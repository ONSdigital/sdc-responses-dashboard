FROM nikolaik/python-nodejs:latest

WORKDIR /app
COPY . /app
EXPOSE 8078

COPY package*.json ./
COPY yarn.lock ./
RUN yarn compile

RUN pip3 install -U pipenv && pipenv install --system --deploy

ENTRYPOINT ["python3"]
CMD ["run.py"]

