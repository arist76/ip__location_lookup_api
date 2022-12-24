FROM python:3.10.6
WORKDIR /application_root

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /application_root/

RUN pip install -r requirements.txt --no-cache-dir
RUN apt update -y && apt upgrade -y
RUN apt install -y postgresql-client

COPY . .