FROM python:3.10
WORKDIR /application_root

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /application_root/

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN python3 api/manage.py makemigrations
RUN python3 api/manage.py migrate
RUN python3 api/manage.py import_csv copy

CMD ["python3", "api/manage.py", "runserver", "0.0.0.0:8000"]

