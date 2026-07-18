import joblib
import pandas as pd

# Load saved objects
model = joblib.load("models/fraud_detector.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")


def predict_fraud(input_data):
    """
    input_data: dictionary
    Returns:
        fraud_probability (%)
        prediction (Fraud / Not Fraud)
    """

    # Dictionary → DataFrame
    df = pd.DataFrame([input_data])

    # Apply preprocessing
    df_processed = preprocessor.transform(df)

    # Predict probability
    probability = float(model.predict(df_processed , verbose=0)[0][0])

    if probability >= 0.5:
        prediction = "Fraud"
    else:
        prediction = "Not Fraud"

    return prediction, probability * 100