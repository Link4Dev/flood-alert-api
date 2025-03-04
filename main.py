from fastapi import FastAPI

# Initialisation de l'application
app = FastAPI()

# Route d'accueil (test)
@app.get("/")
def home():
    return {"message": "Système d'alerte inondation actif"}

# Route pour récupérer les risques d'inondation
@app.get("/api/flood-risk")
def get_flood_risk():
    return {
        "location": {"latitude": 14.6928, "longitude": -17.4467},
        "flood_risk": "Élevé",
        "risk_level": 85,
        "recommendations": ["Évacuer les zones basses", "Suivre les alertes radios"]
    }
}

