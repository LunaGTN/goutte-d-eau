from clean_data import cleaning_csv
from call_api import get_data_from_api_now
from model import main_model
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier


model = RandomForestClassifier()

def predict_rain_with_date(date):
    date = str(datetime.now())[:10]
    data_meteo = get_data_from_api_now(date)
    df = cleaning_csv(data_meteo)
    line = df.tail(1)
    rain_probability =  main_model(model, line)[0][1]
    return rain_probability