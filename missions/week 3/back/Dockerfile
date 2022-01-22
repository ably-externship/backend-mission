FROM python:3.8

RUN apt-get update
RUN apt-get install python3-venv -y
RUN apt-get install default-libmysqlclient-dev -y
RUN apt-get install gcc -y
RUN apt-get install python3-dev -y
RUN apt-get install -y python-setuptools python-dev build-essential

RUN python3 -m venv venv
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]