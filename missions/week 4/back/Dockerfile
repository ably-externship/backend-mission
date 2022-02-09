FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
#COPY requirements.txt /usr/src/app/
COPY . /usr/src/app/
#RUN pip install --default-timeout=100 future
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
