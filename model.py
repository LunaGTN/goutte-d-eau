#Entraîner un modèle de classification supervisé
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import sqlite3

conn = sqlite3.connect("meteo.db")

df = pd.read_sql("SELECT * FROM meteo", conn)

X = df.drop("pluie", axis = 1) #Les fetaures
y = df["pluie"] # La cible

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#model = LogisticRegression().fit(X_train, y_train)

print(df.head(2))