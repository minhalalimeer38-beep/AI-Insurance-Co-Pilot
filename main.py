from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import tempfile
import shutil

from app import insurance_ai

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Insurance Claim API is Running"}


@app.post("/predict")
async def predict(

    image: UploadFile = File(...),

    customer_name: str = Form(...),
    policy_number: str = Form(...),

    age: int = Form(...),
    insured_sex: str = Form(...),

    incident_type: str = Form(...),
    collision_type: str = Form(...),
    incident_severity: str = Form(...),

    number_of_vehicles_involved: int = Form(...),
    witnesses: int = Form(...),

    property_damage: str = Form(...),
    police_report_available: str = Form(...),

    total_claim_amount: float = Form(...),

    auto_make: str = Form(...),
    auto_year: int = Form(...)
):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:

        shutil.copyfileobj(image.file, tmp)

        image_path = tmp.name

    form_data = {

        "customer_name": customer_name,
        "policy_number": policy_number,

        "age": age,
        "insured_sex": insured_sex,

        "incident_type": incident_type,
        "collision_type": collision_type,
        "incident_severity": incident_severity,

        "number_of_vehicles_involved": number_of_vehicles_involved,
        "witnesses": witnesses,

        "property_damage": property_damage,
        "police_report_available": police_report_available,

        "total_claim_amount": total_claim_amount,

        "auto_make": auto_make,
        "auto_year": auto_year
    }

    result = insurance_ai(image_path, form_data)

    return JSONResponse(result)