import json

# pessoas = {
#     'nome': 'Luis',
#     'endereços': [
#         {'rua': 'rua 1', 'numero': 2},
#         {'rua': 'rua 2', 'numero': 3},
#     ],
#     'altura':1.5,
#     'dev': True,
#     'ipso':[1,2,3,4]
# }

# with open ('arquivo_novo.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoas,
#         arquivo,
#         ensure_ascii=False,
#         indent=2)
    

with open('arquivo_novo.json','r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    print(pessoas   )