FROM python:3.11

ARG PACKAGE_NAME=image_classification
ARG VERSION=0.0.1

USER root
RUN apt-get update
RUN pip install --upgrade pip setuptools

RUN mkdir -p /home/agent

ARG WORKDIR=/home/agent

RUN mkdir -p /home/agent/logs
RUN touch /home/agent/logs/app.log

ADD src /home/agent/src
ADD config /home/agent/config
ADD resources /home/agent/resources
ADD requirements.txt /home/agent/requirements.txt

RUN pip install --no-cache-dir -r /home/agent/requirements.txt
ENV PYTHONPATH="${PYTHONPATH}:/home/agent:/home/agent/src"

ENV PYTHONUNBUFFERED=0

EXPOSE 9000

WORKDIR ${WORKDIR}

