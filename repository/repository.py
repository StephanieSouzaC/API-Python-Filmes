from flask import jsonify
import sqlite3

class Repository:
    def __init__(self, conn):
        self.conn = conn

    def select_all(self):
        try:
            sql_select_all = '''SELECT * FROM movies'''
            cur = self.conn.cursor()
            cur.execute(sql_select_all)
            rows = cur.fetchall()
            films_json = []
            for row in rows:
                films_dict = {
                    "id": row[0],
                    "title": row[1],
                    "year": row[2],
                    "genre": row[3],
                    "plot": row[4],
                    "poster_path": row[5]
                }
                films_json.append(films_dict)
            return films_json
        except sqlite3.Error as e:
            return f"Erro ao selecionar os filmes: {e}"

    def select_by_id(self, id):
        try:
            sql_select_all = '''SELECT * FROM movies WHERE id = ?'''
            cur = self.conn.cursor()
            cur.execute(sql_select_all, id)
            row = cur.fetchone()
            film_json = []
            film_dict = {
                "id": row[0],
                "title": row[1],
                "year": row[2],
                "genre": row[3],
                "plot": row[4],
                "poster_path": row[5]
            }
            film_json.append(film_dict)
            return film_json
        except sqlite3.Error as e:
            return f"Erro ao selecionar os filmes: {e}"

    def inset_movie(self, title, year, genre, plot, poster_path):
        try:
            film = (title, year, genre, plot, poster_path)
            sql_insert_movie = '''INSERT INTO movies(title, year, genre, plot, poster_path) VALUES(?, ?, ?, ?, ?)'''
            cur = self.conn.cursor()
            cur.execute(sql_insert_movie, film)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir o filme: {e}")

    def update_movie(self, id, title, year, genre, plot, poster_path):
        try:
            sql_update_movie = '''UPDATE movies SET title=?, year=?, genre=?, plot=?, poster_path=? WHERE id = ?'''
            cur = self.conn.cursor()
            cur.execute(sql_update_movie, (title, year, genre, plot, poster_path, id, ))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao atualizar o filme: {e}")

    def remove_movie(self, id):
        try:
            sql_delete_data = '''DELETE FROM movies WHERE id = ?'''
            cur = self.conn.cursor()
            cur.execute(sql_delete_data, (id, ))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao remover o filme: {e}")