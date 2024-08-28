FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

WORKDIR /srv/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN ls

RUN python manage.py collectstatic --no-input
RUN python manage.py runserver 0.0.0.0:8000

# PRECISA DE UM CONTAINER EXCLUSIVO PARA O BANCO DE DADOS '-_- OU ISSO NUNCA VAI RODAR
