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
                dh_utc DATE PRIMARY KEY,
                temperature FLOAT,
                pression FLOAT,
                humidite INT,
                point_de_rosee FLOAT,
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

def insert_data(request, content):
    try:
        with connexion() as conn:
            cursor = conn.cursor()
            rows = [row[1:] for row in content]
            cursor.executemany(request, rows)
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
    header = next(content)
    col = header[1:]
    columns_sql = ", ".join(col)
    create_table_meteo()
    request = f"""INSERT INTO meteo ({columns_sql}) VALUES (?, ?, ?, ?, ?, ?, ?, ?,?, ?)"""
    insert_data(request, content)

    

if __name__ == "__main__":
    main()
