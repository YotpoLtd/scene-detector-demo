# Define the model class
import os
from io import BytesIO

import cloudpickle
import keras
import mlflow.pyfunc
import numpy as np
import requests
import tensorflow
from PIL import Image
from cv2 import resize


# The class we will use in our predictions - this is what is being saved to
# MLFlow as the "Model" and uses an Artifact (xgboost model)


class SceneryModel(mlflow.pyfunc.PythonModel):
    def __init__(self):
        self.keras_model = None

    def load_context(self, context):
        self.keras_model = keras.models.load_model(context.artifacts["keras_model"])

    def predict(self, context, model_input):
        for index, row in model_input.iterrows():
            image_url = row['image_url']
            response = requests.get(image_url)
            image = Image.open(BytesIO(response.content))
            image = np.array(image, dtype=np.uint8)
            image = resize(image, (224, 224))
            image = np.expand_dims(image, 0)

            predictions_to_return = 5
            preds = self.keras_model.predict(image)[0]
            top_preds = np.argsort(preds)[::-1][0:predictions_to_return]

            # load the class label
            file_name = 'categories_places365.txt'
            if not os.access(file_name, os.W_OK):
                synset_url = 'https://raw.githubusercontent.com/csailvision/places365/master/categories_places365.txt'
                os.system('wget ' + synset_url)
            classes = list()
            with open(file_name) as class_file:
                for line in class_file:
                    classes.append(line.strip().split(' ')[0][3:])
            classes = tuple(classes)

            results = []
            # output the prediction
            for i in range(0, 5):
                results.append(classes[top_preds[i]])

            # Call predict from our artifact
            return results

    def save(self, model_path):
        # The environment our model needs to run in
        conda_env = {
            'channels': ['defaults'],
            'dependencies': [
                'keras={}'.format(keras.__version__),
                'tensorflow={}'.format(tensorflow.__version__),
                'cloudpickle={}'.format(cloudpickle.__version__)
            ],
            'name': 'env'
        }

        # Create an `artifacts` dictionary that assigns a unique name to the saved XGBoost model file.
        # This dictionary will be passed to `mlflow.pyfunc.save_model`, which will copy the model file
        # into the new MLflow Model's directory.

        artifacts = {
            "keras_model": model_path,
        }

        vgg_places = "VGG16_Places365"
        mlflow.pyfunc.save_model(vgg_places, python_model=self, artifacts=artifacts, conda_env=conda_env,
                                 code_path=['scenery_model.py'])
        # mlflow.pyfunc.log_model(
        #     artifact_path=vgg_places,
        #     python_model=self,
        #     artifacts=artifacts,
        #     conda_env=conda_env)
