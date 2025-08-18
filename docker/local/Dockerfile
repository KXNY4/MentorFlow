FROM python:3.12.11-alpine3.22 AS builder
LABEL maintainer="Kxnya"

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements/local.txt /app/local.txt
COPY ./requirements/base.txt /app/base.txt

RUN pip install --upgrade pip &&\
    pip install gunicorn &&\
    pip install -r local.txt

COPY . /app
COPY ./.envs /app/.envs
COPY ./docker/local /app/docker

RUN chmod +x /app/docker/server-entrypoint.sh
RUN chmod +x /app/docker/worker-entrypoint.sh
RUN chmod +x /app/docker/celery-beat-entrypoint.sh