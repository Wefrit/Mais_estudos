from itertools import combinations, permutations, product, groupby


def print_iter(iterator):
    print(*list(iterator),sep='\n')
    print()

# pessoas = ['João', 'Luiz', 'Leticia', 'Joana']

# camisetas = [
#     ['preta','branca'],
#     ['p','m','g']
# ]

# # combinations - ordem não importa, combina uma vez pra cada item

# print_iter(combinations(pessoas,2))

# # permutations - ordem importa, combina todos os itens em cada index

# print_iter(permutations(pessoas,2))

# # product - combina as listas dentro das listas

# print_iter(product(*camisetas))

# groupby - agrupa listas com dicts de acordo com o que você selecionar

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leandro', 'nota': 'B'},
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'C'},
    {'nome': 'Helen', 'nota': 'C'},
    {'nome': 'Julio', 'nota': 'A'},
    {'nome': 'Priscilo', 'nota': 'B'},
]

# primeiro tem que tratar os dados e colocar eles na ordem
def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados,key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
