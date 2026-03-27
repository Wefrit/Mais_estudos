from rich import print
from time import sleep

class Livro:
    def __init__(self, nome, total_paginas):
        self.nome = nome
        self.total_paginas = total_paginas
        self.pagina_atual = 1

        print(f'[blue]Você acabou de abrir o livro [red]\'{self.nome}\'[/red] que tem [green]{self.total_paginas} páginas[/green] no total.\n'
              'Você está na [yellow]página 1[/yellow][/blue]')
    
        
    def avancar_paginas(self,n:int=0):
        atual = 0
        for pagina in range(n+1):
            if self.pagina_atual > self.total_paginas:
                print(f'[red]Você chegou ao final do livro \'{self.nome}\'.')
                break
            else:
                atual += 1
                if atual == n+1:
                    sleep(0.5)
                    print(f'Pág.{self.pagina_atual} > [blue]Você avançou {n} páginas e agora está na página {self.pagina_atual}')
                else: 
                    sleep(0.5)
                    print(f'Pág.{self.pagina_atual} > ',end='')
                self.pagina_atual += 1

l1= Livro('nome', 20)
l1.avancar_paginas(100)
