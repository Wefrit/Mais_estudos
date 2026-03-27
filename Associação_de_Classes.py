# class Carrinho:
#     def __init__(self):
#         self._produtos = []

#     def total(self):
#         return f'O valor total das compras é R${sum([p.preco for p in self._produtos])}'
#     def inserir_produto(self, *produtos):
#         self._produtos += produtos
    
#     def listar_produtos(self):
#         print()
#         for produto in self._produtos:
#             print(produto.nome, produto.preco)
#         print()
    
# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco


# carrinho = Carrinho()
# camiseta = Produto('camiseta', 20.50)
# caneta = Produto('caneta', 1.20)
# carrinho.inserir_produto(camiseta,caneta)
# carrinho.listar_produtos()
# print(carrinho.total())


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []

    def inserir_endereco(self, rua, num):
        self.endereco.append(Endereco(rua, num))
    
    def listar_endereco(self):
        for e in self.endereco:
            print(e.rua, e.num)

    def __del__(self):
        print('Apagando,', self.nome)


class Endereco:
    def __init__(self, rua, num):
        self.rua = rua
        self.num = num

    def __del__ (self):
        print('Apagando,', self.rua, self.num)

cliente = Cliente('Maria')
cliente.inserir_endereco('Av Brasil', 30)
cliente.listar_endereco()   
del cliente