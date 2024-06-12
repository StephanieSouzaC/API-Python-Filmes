from db_connection import create_connection
import sqlite3


def create_table(conn):
    try:
        sql_create_table = """CREATE TABLE IF NOT EXISTS movies (
                                         id integer PRIMARY KEY,
                                         title text NOT NULL,
                                         year integer,
                                         genre text,
                                         plot text,
                                         poster_path text
                                     );"""
        cur = conn.cursor()
        cur.execute(sql_create_table)
        print("Tabela criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela: {e}")


def insert_movie(conn, movie):
    try:
        sql_insert_movie = '''INSERT INTO movies(title, year, genre, plot, poster_path) VALUES(?, ?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql_insert_movie, movie)
        conn.commit()
        print("Filme inserido com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao inserir o filme: {e}")


def exec():
    database = '../movies.db'
    conn = create_connection(database)

    create_table(conn)

    movie_1 = ("Interstellar", 2014, "Adventure, Drama, Sci-Fi",
               "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans",
               "https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg")
    movie_2 = ("Harry Potter and the Deathly Hallows: Part 2", 2011, "Adventure, Family, Fantasy",
               "Harry, Ron, and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts",
               "https://m.media-amazon.com/images/M/MV5BMGVmMWNiMDktYjQ0Mi00MWIxLTk0N2UtN2ZlYTdkN2IzNDNlXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_SX300.jpg")
    movie_3 = ("Star Wars: Episode III - Revenge of the Sith", 2005, "Action, Adventure, Fantasy",
               "Three years into the Clone Wars, Obi-Wan Kenobi pursues a new threat, while Anakin Skywalker is lured by Chancellor Palpatine into a sinister plot to rule the galaxy",
               "https://m.media-amazon.com/images/M/MV5BNTc4MTc3NTQ5OF5BMl5BanBnXkFtZTcwOTg0NjI4NA@@._V1_SX300.jpg")

    insert_movie(conn, movie_1)
    insert_movie(conn, movie_2)
    insert_movie(conn, movie_3)


if __name__ == '__main__':
    exec()
