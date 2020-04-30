#!/bin/sh
export GUNICORN_CMD_ARGS="--statsd-host=${STATSD_HOST} \
                          --statsd-prefix=${STATSD_PREFIX} \
                          --log-config ${WORKDIR}/gunicorn_logging.conf \
                          --config ${WORKDIR}/gunicorn_conf.py \
                          --bind ${SERVER_HOST}:${SERVER_PORT} \
                          --workers ${WORKERS} \
                          --graceful-timeout ${GRACEFUL_TIMEOUT_SECONDS}"

#mlflow models serve -m "runs:/$MODEL_VERSION/$MODEL_NAME/" -h $SERVER_HOST -p $SERVER_PORT --no-conda --workers $WORKERS
export prometheus_multiproc_dir=/tmp
exec gunicorn ${GUNICORN_CMD_ARGS} wsgi:app