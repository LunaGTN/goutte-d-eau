import pandas as pd
from io import StringIO

col_to_drop = ["station_id", "pression_variation_3h", "pluie_6h", "pluie_12h", "ensoleillement", "pluie_24h","temperature_min", "temperature_max", "source", "temperature_sol","radiations","neige_au_sol", "nebulosite", "vent_direction", "vent_rafales_10min", "temps_omm","raw_msg"]

def to_dataframe(data:str):
    if isinstance(data, str) and "\n" in data:
        df = pd.read_csv(StringIO(data), sep=";", comment="#")
    else:
        df = pd.read_csv(data, sep=";", comment="#")
    df = df[df["station_id"] != "string"]
    return df.drop(axis=1, columns=col_to_drop)

def correct_type(df):
    df["visibilite"] = pd.to_numeric(df["visibilite"])
    df["vent_rafales"] = pd.to_numeric(df["vent_rafales"])
    df["pluie_1h"] = pd.to_numeric(df["pluie_1h"])
    df["pluie_3h"] = pd.to_numeric(df["pluie_3h"])
    return df

def fill_na(df):
    df["visibilite"] = df["visibilite"].fillna(df["visibilite"].median())
    df["vent_rafales"] = df["vent_rafales"].fillna(df["vent_rafales"].median())
    df["pluie_1h"] = df["pluie_1h"].fillna(0) #Si null  = pas de pluie
    df["pluie_3h"] = df["pluie_3h"].fillna(df["pluie_1h"]) #Si pluie 3h manquante, considère la pluie de l'heure
    return df

def transform_date(df):
    df["dh_utc"] = pd.to_datetime(df["dh_utc"])
    df["mois"] = df["dh_utc"].dt.month
    df["jour"] = df["dh_utc"].dt.day
    return df.drop(axis=1, columns= ["dh_utc"])

def add_col_rain(df):
    df["pluie"] = (df["pluie_1h"] > 0).astype(int) #Si pluie_1h > 0, il pleut
    return df.drop(columns=["pluie_1h"])

def cleaning_csv(data):
    df = to_dataframe(data)
    df = correct_type(df)
    df = fill_na(df)
    df = transform_date(df)
    df = add_col_rain(df)
    return df

def export_df_to_csv_file(df, filename):
    df.to_csv(f"{filename}.csv")