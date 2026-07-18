def generate_explanation(result):

    explanation = []

    # Damage explanation
    if result["damage_prediction"] == "Severe Damage":
        explanation.append("🔴 AI detected Severe Damage from the uploaded vehicle image.")
    elif result["damage_prediction"] == "Moderate Damage":
        explanation.append("🟠 AI detected Moderate Damage from the uploaded vehicle image.")
    else:
        explanation.append("🟢 AI detected Minor Damage from the uploaded vehicle image.")

    # Confidence
    if result["damage_confidence"] >= 90:
        explanation.append("✅ Model is highly confident about the damage prediction.")
    elif result["damage_confidence"] >= 70:
        explanation.append("✅ Model is reasonably confident about the damage prediction.")
    else:
        explanation.append("⚠ Model confidence is relatively low. Manual inspection is recommended.")

    # Fraud explanation
    if result["fraud_prediction"] == "Fraud":
        explanation.append(
            f"🚨 Fraud probability is {result['fraud_probability']:.2f}%. This claim should be reviewed manually."
        )
    else:
        explanation.append(
            f"✅ Fraud probability is only {result['fraud_probability']:.2f}%. No major fraud indicators were detected."
        )

    return explanation