import copy
# aumente os preços dos produtos em 10%;
# gere novos_produtos
# ordene os produtos por nome decrescente
# gere produtos_ordenados_por_nome 
# ordene os produtos por preço crescente
# gere produtos_ordenados_por preço


produtos = [{'nome': 'Produto 5', 'preco': 10.00},
            {'nome': 'Produto 1', 'preco': 22.32},
            {'nome': 'Produto 3', 'preco': 10.11},
            {'nome': 'Produto 2', 'preco': 105.87},
            {'nome': 'Produto 4', 'preco': 69.90},
            ]

novos_produtos = [{ **produto, 'preco': round(produto['preco'] * 1.1,2)}
            for produto in produtos]

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos),key=lambda produto:produto['nome'], reverse=True)
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda produto:produto['preco'])


print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()
print(*novos_produtos,sep='\n')