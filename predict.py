import argparse

import mlflow.keras
import mlflow.pyfunc
import pandas as pd

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-name')
    parser.add_argument('--model-version')
    parser.add_argument('--image-url')
    args = parser.parse_args()

    scenery_model_path = "runs:/{}/{}/".format(args.model_version, args.model_name)

    args = parser.parse_args()
    mlflow.keras.autolog()
    m = mlflow.pyfunc.load_model(scenery_model_path)
    model_input = pd.DataFrame(data={'image_url': [args.image_url]})
    m.predict(model_input=model_input)
