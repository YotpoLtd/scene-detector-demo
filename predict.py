import mlflow.keras
import mlflow.pyfunc
import pandas as pd

if __name__ == "__main__":
    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("vgg16_places")
    mlflow.keras.autolog()
    m = mlflow.pyfunc.load_model(
        "/Users/rbarabash/Development/yotpo-workspace/scene-detector/VGG16_Places365")
    model_input = pd.DataFrame(data={'image_url': ['http://places2.csail.mit.edu/imgs/demo/6.jpg']})
    m.predict(model_input=model_input)
