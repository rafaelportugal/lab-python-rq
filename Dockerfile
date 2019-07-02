FROM python:3.7.3-slim


RUN apt-get update && apt-get install procps -y

WORKDIR /app
COPY . /app

RUN pip install pipenv
RUN python -m pip install --upgrade pip

RUN pipenv install --system --deploy --ignore-pipfile

