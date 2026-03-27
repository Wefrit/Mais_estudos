# from rich import print

# class Caneta:
#     def __init__(self, cor):
#         escolha = ''
#         match cor.lower().strip():
#             case 'azul':
#                 escolha = '[blue]' 
#             case 'vermelha' | 'vermelho':
#                 escolha = '[red]'
#             case 'verde':
#                 escolha = '[green]'
#         self.cor = escolha
#         self.tampada = True

#     def destampar(self):
#         if self.tampada:
#             self.tampada = False
#         else:
#             print(f'A {self.cor}caneta[/] ja está destampada')

#     def tampar(self):
#         if self.tampada == False:
#             self.tampada = True
#         else:
#             print(f'A {self.cor}caneta[/] ja está tampada')
    
#     def escrever(self,msg):
#         if self.tampada:
#             print(f'A {self.cor}caneta[/] está tampada')
#         else:
#             print(f'{self.cor}{msg}')

#     def quebrar_linha(self, x):
#         print('\n'*(x-1))
        
# caneta_azul = Caneta('azul')
# caneta_vermelha = Caneta('vermelha')
# caneta_verde = Caneta('verde')

# caneta_azul.destampar()
# caneta_vermelha.destampar()
# caneta_verde.destampar()
# caneta_verde.destampar()


# caneta_azul.escrever('akmcka')
# caneta_azul.quebrar_linha(3)
# caneta_verde.escrever('Verde')
# caneta_vermelha.escrever('Vermelha')
# caneta_vermelha.tampar()
# caneta_vermelha.escrever('Vermelha')
# caneta_vermelha.tampar()



clientes = [('nome', 30),('oto nome', 12)]

def older(list):
    nova_lista = []
    for cliente in list:
        if cliente[1] >= 30:
            nova_lista.append(cliente)
    return nova_lista

print(older(clientes))