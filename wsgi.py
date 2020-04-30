import os

from flask import request
from mlflow.pyfunc import scoring_server, load_model
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

app = scoring_server.init(load_model(os.getenv('MODEL_PATH')))
metrics = GunicornPrometheusMetrics(app)

metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)
