FROM ubuntu:latest
LABEL authors="admin"

ENTRYPOINT ["top", "-b"]

RUN pip3 install -r requirements.txt
RUN mkdir media
RUN gunicorn app:app