from clean_data import cleaning_csv
from model import main_model
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from dotenv import load_dotenv
import os
import requests

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


model = RandomForestClassifier()

def predict_rain_with_date(date):
    date = str(datetime.now())[:10]
    data_meteo = get_data_from_api_now(date)
    df = cleaning_csv(data_meteo)
    line = df.tail(1)
    rain_probability =  main_model(model, line)[0][1]
    return rain_probability