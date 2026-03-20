#Entraîner un modèle de classification supervisé
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sqlite3

conn = sqlite3.connect("meteo.db")

df = pd.read_sql("SELECT * FROM meteo", conn)

X = df.drop("pluie", axis = 1) #Les fetaures
y = df["pluie"] # La cible

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

def scaled_data_to_predict(data):
    scaler = StandardScaler()
    scaler.fit(data)
    return scaler.transform(data)


def fit_model(model, data_to_predict_scaled):
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict_proba(data_to_predict_scaled)
    return y_pred

def main_model(model, data_to_pred):
    data_scaled = scaled_data_to_predict(data_to_pred)
    prediction = fit_model(model, data_scaled)
    return prediction

