#Entraîner un modèle de classification supervisé
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
import sqlite3

def train_model_and_scaler():
    conn = sqlite3.connect("./DATA/meteo.db")

    df = pd.read_sql("SELECT * FROM meteo", conn)

    X = df.drop(["pluie", "pluie_1h", "id"], axis = 1) #Les features
    y = df["pluie"] # La cible

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)


    model = RandomForestClassifier(class_weight = 'balanced', min_samples_split=10)
    model.fit(X_train_scaled, y_train)

    with open('MODEL/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

    with open('MODEL/model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':
    train_model_and_scaler()