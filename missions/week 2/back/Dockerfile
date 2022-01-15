FROM python:3.10

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

