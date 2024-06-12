import requests

def switch():
    choice = int(input('''Escolha uma opção
    1: Buscar todos os filmes;
    2: Buscar filme por ID;
    3: Cadastrar filme;
    4: Atualizar filme;
    5: Deletar filme;
    '''))

    if choice == 1:
        get_data()
    elif choice == 2:
        id = int(input('ID que deseja buscar: '))
        get_data_by_id(id)
    elif choice == 3:
        title = input('Digite o título: ')
        year = int(input('Digite o ano: '))
        genre = input('Digite o genero: ')
        plot = input('Digite a sinopse: ')
        poster_path = input('Digite o caminha para imagem do poster: ')
        create_data_movie(title, year, genre, plot, poster_path)
    elif choice == 4:
        id = int(input('Digite o ID do filme que deseja alterar: '))
        title = input('Digite o novo título: ')
        year = int(input('Digite o ano correto: '))
        genre = input('Digite o novo genero: ')
        plot = input('Digite a nova sinopse: ')
        poster_path = input('Digite o caminha para nova imagem do poster: ')
        update_data_movie(id, title, year, genre, plot, poster_path)
    elif choice == 5:
        id = int(input('Digite o ID do filme que deseja DELETAR: '))
        delete_data_movie(id)
    else:
        print('Esse número não faz parte da escolha')

def get_data():
    url = 'http://127.0.0.1:5000/listMovies'

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        print("Posts:", posts)
    else:
        print("Erro ao fazer a requisição:", response.status_code)

def get_data_by_id(id):
    url = f'http://127.0.0.1:5000/listMovies/{str(id)}'

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        print("Posts:", posts)
    else:
        print("Erro ao fazer a requisição:", response.status_code)

def create_data_movie(title, year, genre, plot, poster_path):
    url = 'http://127.0.0.1:5000/addFilm'

    new_post = {
        "title": title,
        "year": year,
        "genre": genre,
        "plot": plot,
        "poster_path": poster_path
    }

    response = requests.post(url, json=new_post)

    if response.status_code == 201:
        post = response.json()
        print("Novo Post Criado:", post)
    else:
        print("Erro ao fazer a requisição:", response.status_code)

def update_data_movie(id, title, year, genre, plot, poster_path):
    url = f'http://127.0.0.1:5000/updateFilm/{str(id)}'

    updated_post = {
        "title": title,
        "year": year,
        "genre": genre,
        "plot": plot,
        "poster_path": poster_path
    }

    response = requests.put(url, json=updated_post)

    if response.status_code == 200:
        post = response.json()
        print("Post Atualizado:", post)
    else:
        print("Erro ao fazer a requisição:", response.status_code)

def delete_data_movie(id):
    url = 'http://127.0.0.1:5000/deleteMovie'
    delete_post = {
        "id": id
    }

    response = requests.delete(url, json=delete_post)

    if response.status_code == 200:
        print("Post deletado com sucesso")
    else:
        print("Erro ao fazer a requisição:", response.status_code)

if __name__ == '__main__':
    switch()