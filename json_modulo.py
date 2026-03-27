import json
import os

# class Movie(TypedDict):
#     title : str
#     original_title : str
#     is_movie : bool
#     imdb_rating : float
#     year : int
#     charcters : list[int]
#     budget : None | float


# str_json = '''
# {
#     "title" : "O Senhor dos Anéis",
#     "original_title" : "Lord of the Rings",
#     "is_movie" : true,
#     "imdb_rating" : 8.8,
#     "year" : 2012,
#     "charcters" : ["Frodo","Sam","Legolas"],
#     "budget" : null
     
# }
# '''

# filme : Movie = json.loads(str_json)

# str_json = json.dumps(filme,ensure_ascii = False, indent = 2)

# print(str_json)

NOME_ARQUIVO = 'json_modulo.json'
CAMINHO_ABSOLUTO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)
print(os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    ))

filme ={
    "title" : "O Senhor dos Anéis",
    "original_title" : "Lord of the Rings",
    "is_movie" : True,
    "imdb_rating" : 8.8,
    "year" : 2012,
    "charcters" : ["Frodo","Sam","Legolas"],
    "budget" : None
     
}

with open(CAMINHO_ABSOLUTO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)
