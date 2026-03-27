# Projet goutte d'eau

**Objectif:** Prédire le risque de pluie pour une ville donnée, en regard d'une date donnée.
**Pré-requis:** 
1. Se rendre sur le site: https://www.infoclimat.fr/
2. Se créer un compte, attendre qu'il soit validé
3. Générer une clé API (⚠️ Une par adresse IP)
3. Télécharger les données d'entraînement du modèle au format csv à la racine 

## Utilisation
### Lors du premier usage:
1. Création de la BDD d'entraînement: 
python3 DATA/create_db.py

2. Entraînement du modèle: Lance le script MODEL/model.py
python3 MODEL/model.py

### Après
Une fois le modèle entraîné, les prédictions sont faites depuis l'interface avec la fonction predict_rain_with_date(main.py)

3. Lancer le serveur local pour l'API:
 uvicorn api:app --host 0.0.0.0 --port 8000

4. Sur un autre terminal, lancer l'interface graphique: 
streamlit run app.py

