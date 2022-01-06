FROM alpine:3.8

RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc && pip3 install --upgrade pip
ENV PYTHONUNBUFFERED 1

COPY ./requirements/common.txt /common.txt
COPY ./requirements/dev.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app