#!/bin/sh
export GUNICORN_CMD_ARGS="--statsd-host=${STATSD_HOST} --statsd-prefix=${STATSD_PREFIX} --log-config ${WORKDIR}/gunicorn_logging.conf"
mlflow models serve -m "runs:/$MODEL_VERSION/$MODEL_NAME/" -h $SERVER_HOST -p $SERVER_PORT --no-conda --workers $WORKERS