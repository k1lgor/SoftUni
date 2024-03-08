# build stage
FROM python:3.10-alpine

WORKDIR /django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip && pip install django psycopg2-binary --no-cache-dir

COPY ./entrypoint.sh .
RUN chmod +x /django/entrypoint.sh

COPY . .

ENTRYPOINT ["/bin/sh", "/django/entrypoint.sh"]
