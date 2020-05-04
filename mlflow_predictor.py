import argparse
import base64

import mlflow.keras
import mlflow.pyfunc
import pandas as pd
import requests

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-path')
    parser.add_argument('--image-url')
    args = parser.parse_args()
    mlflow.keras.autolog()
    model = mlflow.pyfunc.load_model(args.model_path)
    image_contents = base64.encodebytes(requests.get(args.image_url).content)
    model_input = pd.DataFrame(data={'image_bytes': [image_contents]})
    model.predict(model_input=model_input)
