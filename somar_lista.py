# Considerando duas listas  de inteiros ou floats (lista a e b), some os valores nas listas  retornando uma nova lista
# com os valores somados:

# Se uma lista  for maior que a outra, a soma vai considerar o tamanho da menor

# exemplo: lista_a = [1,2,3,4,5,6,7]
# lista_b = [1,2,3,4]

#resultado [2,4,6,8 ]


lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

def soma_listas(lista1, lista2):
    length = min(len(lista1),len(lista2))
    return [lista1[i]+lista2[i] for i in range(length)]

print(soma_listas(lista_a, lista_b))