FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY . /code


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


