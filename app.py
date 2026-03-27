import streamlit as st
from datetime import datetime
import requests
import subprocess

st.title("Prédire le risque de pluie")
st.subheader("A partir de la date du jour")
st.write(
    "Outil qui récupère les données météo du jour depuis une API OpenData. Un modèle de ML pré-entraîné sur les données de 2025 renvoie une probabilité de pluie sur la journée.")

if st.button("Faire la prédiction"):
    subprocess.run(["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"])
    date = str(datetime.now())[:10]
    response = requests.get(f'http://0.0.0.0:8000/predict/?date={date}')
    if response.status_code == 200:
        print(response.text)
        data = response.json()
        proba = data.get("rain_probability")
        st.write(f"Le probabilité de pluie pour aujourd'hui (le {date}) est de {round(float(proba)*100)}% !")

    else:
        print(f"Request failed with status code {response.status_code}")

    st.balloons()