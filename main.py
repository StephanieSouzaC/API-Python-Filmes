from flask import Flask, redirect, jsonify, request
from db_connection import create_connection
from repository.repository import Repository
from model.films import Films

app = Flask(__name__)
conn = create_connection('movies.db')
repository = Repository(conn)

@app.route('/')
def index():
    return redirect('/listMovies', code=302)

@app.route('/listMovies', methods=['GET'])
def listMovies():
    return jsonify(repository.select_all()), 200

@app.route('/listMovies/<int:id>', methods=['GET'])
def listMoviesById(id):
    return jsonify(repository.select_by_id(str(id))), 200

@app.route('/addFilm', methods=['POST'])
def addFilm():
    try:
        film = Films(request.json['title'], request.json['year'], request.json['genre'], request.json['plot'], request.json['poster_path'])
        repository.inset_movie(film.title, film.year, film.genre, film.plot, film.poster_path)
        return jsonify({'mensage': 'Filme add com sucesso'}), 201
    except KeyError as e:
        return jsonify({'mensage': f'Erro ao tentar incluir o Filme, o campo: {e} está faltando'}), 400

@app.route('/updateFilm/<int:id>', methods=['PUT'])
def updateFilm(id):
    try:
        film = Films(request.json['title'], request.json['year'], request.json['genre'], request.json['plot'], request.json['poster_path'])
        repository.update_movie(str(id), film.title, film.year, film.genre, film.plot, film.poster_path)
        return jsonify({'mensage': 'Filme atualizado com sucesso'}), 200
    except KeyError as e:
        return jsonify({'mensage': f'Erro ao tentar atualizar o Filme, o campo: {e} está faltando'}), 400

@app.route('/deleteMovie', methods=['DELETE'])
def deleteMovie():
    try:
        id = request.json['id']
        repository.remove_movie(str(id))
        return jsonify({'mensage': 'Filme deletado com sucesso'}), 200
    except KeyError as e:
        return jsonify({'mensage': f'Erro ao tentar deletar o Filme, o campo: {e} está faltando'}), 400

if __name__ == '__main__':
    app.run()
