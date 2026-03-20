import streamlit as st
from datetime import datetime
import requests

st.title("Prédire le risque de pluie")
st.subheader("A partir de la date du jour")
st.write("Outil qui récupère les données météo du jour depuis une API OpenData. Un modèle de ML pré-entraîné sur les données de 2025 renvoie une probabilité de pluie sur la journée.")

if st.button("Faire la prédiction"):
    date = datetime.now()
    response = requests.get(f'http://127.0.0.1:8000/predict/?date={date}')
    if response.status_code == 200:
        data = response.json()
        st.write(data)
    else:    
        print(f"Request failed with status code {response.status_code}")   
        
    st.balloons()