FROM python:3.8

MAINTAINER fabio.delvalle@gmail.com

RUN apt-get update -y 

ENV PYTHONUNBUFFERED 1
ENV LIBRARY_PATH=/lib:/usr/lib

RUN apt-get install tzdata \
        && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
        && echo "America/Sao_Paulo" > /etc/timezone

RUN mkdir /src
WORKDIR /src
COPY . /src/
RUN pip install -r core/requirements.txt
#RUN python manage.py makemigrations
#RUN python manage.py migrate

