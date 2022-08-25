# syntax=docker/dockerfile:1

FROM ubuntu:20.04 as josephstool
ENV DEBIAN_FRONTEND noninteractive

COPY . .
RUN apt-get update
RUN apt-get -y install \
  ffmpeg python3 python3-dev python3-pip
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

CMD [ "./result.sh"]