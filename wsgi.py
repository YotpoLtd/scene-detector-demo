import os

from flask import request
from mlflow.pyfunc import scoring_server, load_model
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

path = "runs:/{}/{}/".format(os.getenv('MODEL_VERSION'), os.getenv('MODEL_NAME'))
app = scoring_server.init(load_model(path))
metrics = GunicornPrometheusMetrics(app)

metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)
