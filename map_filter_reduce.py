from functools import reduce, partial

# map / partial - cria funções de closure 

produtos = [
    {'nome':'Produto 5', 'preco':10},
    {'nome':'Produto 1', 'preco':22},
    {'nome':'Produto 3', 'preco':10},
    {'nome':'Produto 2', 'preco':105},
    {'nome':'Produto 4', 'preco':69},
]

def aumentar_procentagem(valor, porcentagem):
    return round(valor*porcentagem)

aumentar_dez_porcento = partial(aumentar_procentagem, porcentagem=1.1) #cria uma closure diretamente com partial

def muda_preco(produto):
    return{
        **produto,'preco':aumentar_dez_porcento(produto['preco'])
    } # faz list comprehension dentro da função pra mapear depois

novos_produtos=list(map(
                muda_preco,
                produtos
            )
)

# print(*novos_produtos,sep='\n')

# filter - filtra usando função de mapeamento

novos_produtos_filtrados = filter(lambda p:p['preco'] > 10,
                                  novos_produtos)

print(*novos_produtos_filtrados,sep='\n')

# reduce - reduz valores em uma some de um único valor

total = reduce(
    lambda a,p:a+p['preco'], # a é o acumulador com valor 0 no 3 parametro, p é a chave que vai ser usado de referência (preco) do iterável
    novos_produtos,
    0
)

print(total)