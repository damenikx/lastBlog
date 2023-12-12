FROM python:3.10-alpine3.13

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /lastBlog/app

RUN pip install --upgrade pip
COPY requirements.txt /lastBlog/app
RUN pip install -r requirements.txt

COPY . .
