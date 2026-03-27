from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        etiqueta = Panel(f'\t   {self.nome}\n - - - - - - - - - - - - - -\n....... Preço R${self.preco:,.2f} ........',title='Produto', expand=False,)
        return etiqueta
    


p1=Produto('Lapis', 2.5)
p2 = Produto('Iphone', 8_000_000)
print(p2.etiqueta())



