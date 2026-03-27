# Crie uma função zipper, o trabalho dessa função será unir duas listas na ordem.
# use todos os valores da menor lista
# [salvador, ubatuba, belo horizonte]
# [ba , sp, mg, rj]
# resultado : [(salvador, ba),(ubatuba, sp), (belo horizonte, mg)]

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(intervalo_maximo)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1,l2))