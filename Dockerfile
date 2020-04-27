FROM python:3.6.5

ENV SERVER_HOST 0.0.0.0

ENV WORKDIR /opt/scene-detector
ENV PYTHONPATH /opt/scene-detector

WORKDIR $WORKDIR

COPY requirements.txt requirements.txt
COPY scenery_model.py scenery_model.py
COPY gunicorn_logging.conf gunicorn_logging.conf
COPY entrypoint.sh /

RUN pip install -r requirements.txt
EXPOSE $SERVER_PORT
#EXEC

ENTRYPOINT ["/entrypoint.sh"]