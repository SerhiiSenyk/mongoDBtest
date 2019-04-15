FROM python:3.6-alpine

RUN adduser -D read

WORKDIR /home/serhii
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY templates templates

COPY read.py  boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP read.py

RUN chown -R read:read ./
USER read

EXPOSE 8000
ENTRYPOINT ["./boot.sh"]
