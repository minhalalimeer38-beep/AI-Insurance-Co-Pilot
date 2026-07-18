from utils.image_predict import predict_damage
from utils.fraud_predict import predict_fraud


def insurance_ai(image_path, form_data):
    """
    Parameters
    ----------
    image_path : str
        Path of uploaded car image

    form_data : dict
                {
                    "customer_name"               : "...",
                    "policy_number"               : "...",
                    "age"                         : ...,
                    "insured_sex"                 : "...",
                    "incident_type"               : "...",
                    "collision_type"              : "...",
                    "incident_severity"           : "...",
                    "number_of_vehicles_involved" : ...,
                    "witnesses"                   : ...,
                    "property_damage"             : "...",
                    "police_report_available"     : "...",
                    "total_claim_amount"          : ...,
                    "auto_make"                   : "...",
                    "auto_year"                   : ... 
                }
            """

    damage, confidence = predict_damage(image_path)

    damage_labels = {
    "01-minor"    : "Minor Damage",
    "02-moderate" : "Moderate Damage",
    "03-severe"   : "Severe Damage"
}

    damage = damage_labels.get(damage, damage)

    sample = {
            "age": form_data["age"],
            "insured_sex"                 : form_data["insured_sex"],
            "incident_type"               : form_data["incident_type"],
            "collision_type"              : form_data["collision_type"],
            "incident_severity"           : form_data["incident_severity"],
            "number_of_vehicles_involved" : form_data["number_of_vehicles_involved"],
            "witnesses"                   : form_data["witnesses"],
            "property_damage"             : form_data["property_damage"],
            "police_report_available"     : form_data["police_report_available"],
            "total_claim_amount"          : form_data["total_claim_amount"],
            "auto_make"                   : form_data["auto_make"],
            "auto_year"                   : form_data["auto_year"]
             }

    fraud_prediction, fraud_probability = predict_fraud(sample)

    result = {
            "customer_name"     : form_data["customer_name"],
            "policy_number"     : form_data["policy_number"],
            "damage_prediction" : damage,
            "damage_confidence" : confidence,
            "fraud_prediction"  : fraud_prediction,
            "fraud_probability" : fraud_probability,
            "claim_amount"      : form_data["total_claim_amount"],
            "vehicle_make"      : form_data["auto_make"],
            "vehicle_year"      : form_data["auto_year"]
             }

    return result