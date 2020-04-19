FROM continuumio/miniconda:4.7.12

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

ENV SERVER_PORT 5000
ENV SERVER_HOST 0.0.0.0

ENV ARTIFACT_STORE /opt/mlflow/artifactStore
ENV PYTHONPATH /opt/mlflow/utils

RUN apt-get update && apt-get install -y python3-dev gcc g++ zip && rm -rf /var/lib/apt/lists/*
RUN pip install awscli
RUN aws s3 cp s3://yotpo-data-config/emr/pip/pip.prod.conf /root/.pip/pip.conf

WORKDIR /scenery
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /opt/mlflow/scripts \
&& mkdir -p ${ARTIFACT_STORE}

# Copy over artifact and code
COPY scenery_model.py /opt/mlflow/utils/
COPY /temp_artifacts/ ${ARTIFACT_STORE}/

EXPOSE $SERVER_PORT

#EXEC

COPY entrypoint.sh /
CMD ["/entrypoint.sh"]