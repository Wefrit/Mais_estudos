from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, nome:str, nick:str='Player'):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self,jogo:str):
        self.jogos.append(jogo)

    def ficha(self):
        jogos_formatados = '\n'.join([jogo for jogo in self.jogos])
        ficha = Panel(title=f'Jogador <{self.nick}>', title_align='center',
                      renderable=f'Nome Real: [bold black on blue]{self.nome}[/bold black on blue]\n'
                      f'Jogos favoritos:\n'
                      f'[blue]{jogos_formatados}',
                      expand=False)
        return ficha


g1 = Gamer('OLA', 'Lili')
g1.add_favoritos('jogo1')
g1.add_favoritos('jogo2')
print(g1.ficha())