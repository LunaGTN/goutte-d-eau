from dotenv import load_dotenv
import os
import requests
from fastapi import FastAPI
from main import predict_rain_with_date

#API_METEO
BASE_URL = "https://www.infoclimat.fr/opendata/"

load_dotenv()
KEY = os.getenv("API_KEY")

def get_data_from_api_now(date):
    #date = str(datetime.now())[:10]
    params = {
    "version": 2,
    "method": "get",
    "format": "csv",
    "stations[]": "07630",
    "start": date,
    "end": date,
    "token": KEY
}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return "Erreur :", response.status_code


#MON_API
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "API qui renvoie une probabilité de pluie"}

@app.post("/predict/")
async def predict_rain(date):
    return {"rain_probability": predict_rain_with_date(date)}


