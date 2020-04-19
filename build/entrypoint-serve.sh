#!/bin/sh
mlflow models serve -m $ARTIFACT_STORE -h $SERVER_HOST -p $SERVER_PORT --no-conda