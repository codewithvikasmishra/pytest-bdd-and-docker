#From creates a lyer from the ubuntu:18.04 Docker image.
#COPY adds files from Docker client's current directory.
#RUN builds your application with make.
#CMD specifies what command to run within the container.

FROM python:3.7
MAINTAINER Vikas Kumar Mishra
copy requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update -y

COPY . /app
WORKDIR /app