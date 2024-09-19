FROM python:latest

ADD app/ server/
ADD main.py server/

WORKDIR /server/