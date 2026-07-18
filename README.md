---
title: AI Insurance Claim API
emoji: 🚗
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
license: mit
---

# 🚗 AI Insurance Claim Co-Pilot

An AI-powered Insurance Claim Processing System built using **Deep Learning**, **Artificial Intelligence**, **FastAPI**, and **Streamlit**.

The system automatically:

- 🚗 Detects vehicle damage from uploaded images
- 🛡 Predicts insurance fraud using an Artificial Neural Network (ANN)
- 🧠 Generates Explainable AI (XAI)
- 📄 Creates a professional PDF report

---

# Features

- Damage Detection using EfficientNetB0
- Insurance Fraud Detection using ANN
- Explainable AI
- PDF Report Generation
- FastAPI Backend
- Streamlit Frontend

---

# Models

## Damage Detection

- EfficientNetB0
- TensorFlow / Keras
- Image Classification

Classes:

- Minor Damage
- Moderate Damage
- Severe Damage

---

## Fraud Detection

- Artificial Neural Network (ANN)
- TensorFlow / Keras

Input Features:

- Age
- Gender
- Incident Type
- Collision Type
- Incident Severity
- Number of Vehicles
- Witnesses
- Property Damage
- Police Report
- Claim Amount
- Vehicle Make
- Vehicle Year

---

## Prediction

POST /predict

Returns:

- Damage Prediction
- Damage Confidence
- Fraud Prediction
- Fraud Probability
- Claim Information

---

# Tech Stack

- Python
- FastAPI
- Streamlit
- TensorFlow
- Keras
- Scikit-learn
- Pandas
- NumPy
- ReportLab

---

# Folder Structure

```
AI-Copilot/

│── main.py
│── app.py
│── requirements.txt
│── models/
│── utils/
│── README.md
```

---

Built for AI Innovation Hackathon 2026 🚀
