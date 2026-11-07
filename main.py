import os

from fastapi import FastAPI
import pandas as pd
import joblib

# Initialisation de FastAPI
app = FastAPI(
    title="Healthcare AI API",
    description="API de prédiction pour le modèle Random Forest",
    version="1.0"
)

# Chargement de modèle
MODEL_PATH = "model.pkl"
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
    print("Modèle chargé avec succès.")
else:
    model = None
    print("Attention : model.pkl introuvable.")


@app.post("/predict")
def predict_patient(
        age: int,
        gender: str,
        blood_type: str,
        medical_condition: str,
        admission_type: str,
        medication: str,
        billing_amount: float,
        insurance_provider: str
):
    # Structuration des données entrantes comme DataFrame
    input_data = pd.DataFrame({
        'Age': [age],
        'Gender': [gender],
        'Blood Type': [blood_type],
        'Medical Condition': [medical_condition],
        'Admission Type': [admission_type],
        'Medication': [medication],
        'Billing Amount': [billing_amount],
        'Insurance Provider': [insurance_provider]
    })

    # Prédiction avec modèle
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)

    # Retour du résultat en JSON
    return {
        "resultat_predit": prediction[0],
        "probabilites": probabilities[0].round(2).tolist()
    }