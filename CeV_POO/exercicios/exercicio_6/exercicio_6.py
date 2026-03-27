from rich.panel import Panel
from rich import print
import rich

class Churrasco:
    PRECO_KG = 82.4
    MEDIA_CARNE_PESSOA = .4 

    def __init__(self, nome:str, n_de_pessoas:int):
        self.nome = nome
        self.n_de_pessoas = n_de_pessoas

    def calculo(self):
        total_carne = self.n_de_pessoas * .4
        custo_total = total_carne * 82.4
        custo_individual = custo_total / self.n_de_pessoas
        
        caixa = Panel(
            title=self.nome, 
            renderable=f'Analisando [green]{self.nome}[/green] com [blue]{self.n_de_pessoas}[/blue].\n'
            f'Cada partiipante comerá 0.4Kg e cada Kg custa  R$82.40.\n'
            f'Recomendado comprar [blue]{total_carne}Kg[/blue] de carne\n'
            f'O custo total será de [green]R${custo_total:.2f}[/green].\n'
            f'Cada pessoa pagará [yellow]R${custo_individual:.2f}[/yellow]',
            expand=False
        )
        return caixa


c1 = Churrasco('Churras dos cria', 5)

print(c1.calculo())