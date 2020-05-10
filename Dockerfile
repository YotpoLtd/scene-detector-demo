FROM python:3.6.5

ENV SERVER_HOST 0.0.0.0

ENV WORKDIR /opt/scene-detector
ENV PYTHONPATH /opt/scene-detector

WORKDIR $WORKDIR

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY gunicorn_logging.conf gunicorn_logging.conf
COPY gunicorn_conf.py gunicorn_conf.py
COPY wsgi.py wsgi.py
COPY entrypoint.sh /

EXPOSE $SERVER_PORT

ENTRYPOINT ["/entrypoint.sh"]