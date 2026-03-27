import sqlite3
import csv
from clean import export_df_to_csv_file, cleaning_csv
from time import sleep

def connexion():
    return sqlite3.connect("DATA/meteo.db")

def create_table_meteo():
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            request = """
            CREATE TABLE IF NOT EXISTS Meteo(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                temperature FLOAT,
                pression FLOAT,
                humidite INT,
                point_de_rosee FLOAT,
                visibilite INT,
                vent_moyen FLOAT,
                pluie_1h FLOAT,
                mois INT,
                jour INT,
                heure INT,
                pluie INT
            )
            """
            cursor.execute(request)
            conn.commit()
    except Exception as e:
        print(f"Une erreur est survenue lors de la création de la table: {e}")

def insert_data(request, content):
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            rows = [row[1:] for row in content]
            cursor.executemany(request, rows)
            conn.commit()
    except Exception as e:
        print(f"Une erreur est survenue lors de l'insertion dans la table: {e}")


def get_csv_content():
    file = open('DATA/data_clean.csv')
    content =  csv.reader(file)
    return content

def build_db(content):
    header = next(content)
    col = header[1:]
    columns_sql=  ", ".join(col)
    create_table_meteo()
    request = f"""INSERT INTO meteo ({columns_sql}) VALUES (?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?)"""
    return request

def main(path_source):
    df = cleaning_csv(path_source) #nettoie
    export_df_to_csv_file(df, "DATA/data_clean") #exporte
    sleep(2)
    content = get_csv_content()
    request = build_db(content)
    insert_data(request, content)
    return df

    

if __name__ == "__main__":
    df = main("data_from_website.csv")
    print(df.head(1))
