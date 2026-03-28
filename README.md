# Projet goutte d'eau

**Objectif:** Réaliser un modèle de prédiction du risque de pluie pour une ville donnée, ici la ville de Blagnac, avec une date donnée.
Il s'agit ici de développer un MVP, qui sera donc voué à évoluer, et à être amélioré. 

**Pré-requis:** 
1. Se rendre sur le site: https://www.infoclimat.fr/
2. Se créer un compte, attendre qu'il soit validé
3. Générer une clé API (⚠️ Une par adresse IP)
3. Télécharger les données d'entraînement du modèle au format csv à la racine (data_from_website.csv)

## Utilisation
### Lors du premier usage
1. Création de la BDD d'entraînement: 
python3 DATA/create_db.py

2. Entraînement du modèle: Lance le script MODEL/model.py
python3 MODEL/model.py

### A chaque utilisation
Une fois le modèle entraîné, les prédictions sont faites depuis l'interface avec la fonction predict_rain_with_date(date) depuis le fichier main.py

3. Lancer le serveur local pour l'API:
 uvicorn api:app --host 0.0.0.0 --port 8000

4. Sur un autre terminal, lancer l'interface graphique: 
streamlit run app.py

## Autre
Evaluation du modèle présente dans le fichier MODEL/eval_model.ipynb