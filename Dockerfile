# pull official base image
FROM python:3.9.-alpine

# set work directory
WORKDIR /Users/smallbudget4bigname/django_projects/myshop

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .