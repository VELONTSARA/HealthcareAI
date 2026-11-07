from fastapi import FastAPI
import pandas as pd
import joblib

# Initialisation de l'application FastAPI
app = FastAPI(
    title="Healthcare AI API",
    description="API de prédiction pour le modèle Random Forest",
    version="1.0"
)

# Chargement de votre modèle .pkl au démarrage
model = joblib.load('model.pkl')


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
    # Structuration des données entrantes sous forme de DataFrame
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

    # Prédiction avec le modèle
    prediction = model.predict(input_data)
    probabilities = model.predict_proba(input_data)

    # Retour du résultat au format JSON
    return {
        "resultat_predit": prediction[0],
        "probabilites": probabilities[0].round(2).tolist()
    }