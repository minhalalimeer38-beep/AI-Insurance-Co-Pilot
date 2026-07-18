import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Load trained model
model = load_model("models/best_efficientnet.keras")

# Class names (training folders ke order ke mutabiq)
class_names = [
                "01-minor", 
                "02-moderate", 
                "03-severe"
              ]


def predict_damage(img_path):
    """
    Predict car damage severity from image.
    Returns:
        predicted_class (str)
        confidence (float)
    """

    # Load image
    img = image.load_img(img_path, target_size=(224, 224))

    # Convert to array
    img_array = image.img_to_array(img)

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    predictions = model.predict(img_array, verbose=0)

    predicted_index = np.argmax(predictions)

    predicted_class = class_names[predicted_index]

    confidence = float(np.max(predictions) * 100)

    return predicted_class, confidence





if __name__ == "__main__":

    prediction, confidence = predict_damage(
        "samples_files/car_image.jpg"
    )

    print(prediction)
    print(confidence)