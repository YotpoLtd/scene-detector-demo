#!/bin/sh
export GUNICORN_CMD_ARGS="--statsd-host=${STATSD_HOST:-localhost:8125} \
                          --statsd-prefix=${STATSD_PREFIX:-image_quality} \
                          --log-config ${WORKDIR}/gunicorn_logging.conf \
                          --config ${WORKDIR}/gunicorn_conf.py \
                          --bind ${SERVER_HOST}:${SERVER_PORT} \
                          --workers ${WORKERS:-1} \
                          --threads ${THREADS:-1} \
                          --graceful-timeout ${GRACEFUL_TIMEOUT_SECONDS:-5} \
                          --timeout ${TIMEOUT:-60}"

#Notice here we are not running mlflow models serve directly, this is because we modify the app and registered our middleware
#${GUNICORN_CMD_ARGS} mlflow models serve -m "runs:/$MODEL_VERSION/$MODEL_NAME/" -h $SERVER_HOST -p $SERVER_PORT --no-conda --workers $WORKERS

export prometheus_multiproc_dir=/tmp
exec gunicorn ${GUNICORN_CMD_ARGS} wsgi:app