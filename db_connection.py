import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        print(f"Conectado ao banco de dados SQLite: {db_file}")
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados SQLite: {e}")
    return conn

