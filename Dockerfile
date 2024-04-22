# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /data

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=hello.py
ENV FLASK_DEBUG=1

EXPOSE 5000
EXPOSE 5678

CMD python -m debugpy --listen 0.0.0.0:5678 -m flask run --host=0.0.0.0 --debug
# CMD python -m debugpy --listen 0.0.0.0:5678 -m run_dev.py
