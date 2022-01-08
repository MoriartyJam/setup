# FROM python:3.8
# COPY . /setup_1
# ENV PYTHONUNBUFFERED=1
# WORKDIR /setup_1
# RUN pip install -r requirements.txt
# RUN pip install --upgrade pip
# CMD [ "python", "manage.py", "runserver" ]



# pull official base image
FROM python:3.8
# set work directory
WORKDIR /setup_1
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .