from abc import ABC, abstractmethod
from random import randint, choice

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
        self.curas = []

    def atacar(self, alvo, forca):
        ataque = randint(0, forca)
        golpe = choice(self.golpes)
        print(f'{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com {golpe} de força {forca}')
        self.apanhar(alvo, ataque)

    def apanhar(self, alvo, dano):
        print(f'{alvo.nome}({alvo.vida}) recebeu dano de {dano}!')
        alvo.vida -= dano

    def curar(self):
        tipo = choice(self.curas)
        cura = randint(1,100)
        print(f'{self.nome}({self.vida}) usou {tipo} e curou {cura}')

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Chute Giratório']
        self.curas = ['Atadura', 'Cura de guerra']
    
class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Magia','Sopro Congelante', 'Ventania']
        self.curas = ['Poção de cura', 'Magia de heal']

