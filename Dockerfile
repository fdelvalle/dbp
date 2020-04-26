FROM python:3.8

MAINTAINER fabio.delvalle@gmail.com

RUN apt-get update -y 

ENV PYTHONUNBUFFERED 1
ENV LIBRARY_PATH=/lib:/usr/lib
ENV DJANGO_SETTINGS_MODULE=core.settings.container

RUN apt-get install tzdata \
        && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
        && echo "America/Sao_Paulo" > /etc/timezone

RUN mkdir /src
WORKDIR /src
COPY . /src/
RUN pip install -r core/requirements.txt

