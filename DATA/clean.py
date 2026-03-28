import pandas as pd
from io import StringIO

col_to_drop = ["station_id","pression_variation_3h", "pluie_3h", "pluie_6h", "pluie_12h", "ensoleillement", "vent_rafales",  "pluie_24h","temperature_min", "temperature_max", "source", "temperature_sol","radiations","neige_au_sol", "nebulosite", "vent_direction", "vent_rafales_10min", "temps_omm","raw_msg"]

def file_to_dataframe(file_path:str):
    df = pd.read_csv(file_path, sep=";", comment="#")
    df = df.loc[df["station_id"] != "string"]
    return df.drop(columns=col_to_drop)

def data_to_dataframe(raw_data:str):
    df = pd.read_csv(StringIO(raw_data), sep=";", comment="#")
    df = df.iloc[1:].reset_index(drop=True)
    df = df[df["station_id"] != "string"]
    return df.drop(columns=col_to_drop)

def correct_type(df):
    df["visibilite"] = pd.to_numeric(df["visibilite"])
    df["pluie_1h"] = pd.to_numeric(df["pluie_1h"])
    return df

def fill_na(df):
    df["visibilite"] = df["visibilite"].fillna(df["visibilite"].median())
    df["pluie_1h"] = df["pluie_1h"].fillna(0) #Si null  = pas de pluie
    return df

def transform_date(df):
    df["dh_utc"] = pd.to_datetime(df["dh_utc"])
    df["mois"] = df["dh_utc"].dt.month
    df["jour"] = df["dh_utc"].dt.day
    df["heure"] = df["dh_utc"].dt.hour
    return df.drop(columns= ["dh_utc"])

def add_col_rain(df):
    df["pluie"] = (df["pluie_1h"] > 0).astype(int) #Si pluie_1h > 0, il pleut
    return df

def cleaning_csv(data):
    print(data)
    try:
        df = file_to_dataframe(data)
    except:
        df = data_to_dataframe(data)
    df = correct_type(df)
    df = fill_na(df)
    df = transform_date(df)
    df = add_col_rain(df)
    return df

def export_df_to_csv_file(df, filename):
    df.to_csv(f"{filename}.csv")

if __name__ == "__main__":
    df = cleaning_csv("data_from_website.csv")
    export_df_to_csv_file(df, "DATA/data_clean")