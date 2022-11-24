FROM python:2.7.18-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install psycopg2 dependencies
RUN apt-get update && \
    apt-get install -y libpq-dev gcc

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /usr/src/logs/

# copy project
COPY ./notifications .
