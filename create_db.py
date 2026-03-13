import sqlite3
import csv

def connexion():
    return sqlite3.connect("meteo.db")

def create_table_meteo():
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            request = """
            CREATE TABLE IF NOT EXISTS Meteo(
                date_utc DATE PRIMARY KEY,
                temperature FLOAT,
                pression FLOAT,
                humidite INT,
                point_de_rose FLOAT,
                visibilite INT,
                vent_moyen FLOAT,
                vent_rafales FLOAT,
                pluie_3h FLOAT,
                pluie INT
            )
            """
            cursor.execute(request)
            conn.commit()
    except Exception as e:
        print(f"Une erreur est survenue lors de la création de la table: {e}")

def insert_data(request, csv_ontent):
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            cursor.executemany(request, csv_ontent)
            conn.commit()
    except Exception as e:
        print(f"Une erreur est survenue lors de l'insertion dans la table: {e}")


def get_csv_content(file_path:str):
    file = open('data_clean.csv')
    content =  csv.reader(file)
    return content

def main():
    file_path = "data_clean.csv"
    content = get_csv_content(file_path)
    col = tuple(next(content)[1:])
    create_table_meteo()
    request = f"""INSERT INTO meteo {col}, VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    insert_data(request, content)
    

if __name__ == "__main__":
    main()
