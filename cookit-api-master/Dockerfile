FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

WORKDIR /srv/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /srv/app/
RUN python manage.py collectstatic --no-input
RUN python manage.py runserver 0.0.0.0:8080

#RUN python manage.py collectstatic --no-input