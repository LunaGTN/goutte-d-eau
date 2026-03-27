from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from dotenv import load_dotenv
import os
import requests
import pickle
from DATA.clean import cleaning_csv

#API_METEO
BASE_URL = "https://www.infoclimat.fr/opendata/"

load_dotenv()
KEY = os.getenv("API_KEY")

with open('MODEL/scaler.pkl', 'rb') as f:
    SCALER = pickle.load(f)

# Charger le modèle
with open('MODEL/model.pkl', 'rb') as f:
    MODEL = pickle.load(f)

def get_data_from_api_now(date):
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
        return f"Erreur : {response.status_code} - {response.text}"


model = RandomForestClassifier()

def predict_rain_with_date(date):
    #date = str(datetime.now())[:10]
    data_meteo = get_data_from_api_now(date)
    df = cleaning_csv(data_meteo)
    last_hour_data = df.tail(1).drop(columns=['pluie_1h', 'pluie'])
    scaled_data = SCALER.transform(last_hour_data)
    probabilities = MODEL.predict_proba(scaled_data)[0]
    rain_probability =  str(probabilities[1])
    return rain_probability

if __name__ == '__main__':
    print(predict_rain_with_date("2026-03-26"))
