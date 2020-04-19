import mlflow.keras
import mlflow.pyfunc

from scenery_model import SceneryModel
from keras_models.models.pretrained import vgg16_places365

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("vgg16_places")
    model = vgg16_places365.VGG16_Places365()
    model.save(filepath="artifacts/keras_model.h5", overwrite=True)
    mlflow.keras.autolog()

    sm = SceneryModel()
    sm.save("artifacts/keras_model.h5")
