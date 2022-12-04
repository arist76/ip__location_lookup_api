FROM python:3.10
WORKDIR /application_root

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /application_root/

RUN pip install -r requirements.txt --no-cache-dir

COPY . /application_root/

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py import_csv copy
