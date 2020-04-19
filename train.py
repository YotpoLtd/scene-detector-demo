import argparse

import mlflow.keras
import mlflow.pyfunc
from keras_models.models.pretrained import vgg16_places365

from scenery_model import SceneryModel

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--artifact-path')
    args = parser.parse_args()

    model = vgg16_places365.VGG16_Places365()
    model.save(filepath=args.artifact_path, overwrite=True)
    mlflow.keras.autolog()

    sm = SceneryModel()
    sm.save(args.artifact_path)
