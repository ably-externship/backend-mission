FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./requirements/common.txt /common.txt
COPY ./requirements/prod.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY . .
EXPOSE 8000
CMD ["python","manage.py", "runserver", "--settings=base.settings.prod", "0.0.0.0:8000"]
