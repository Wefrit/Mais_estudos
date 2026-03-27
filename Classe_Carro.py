# Criar um classe Carro,
# Criar uma classe Motor,
# Criar uma classe Fabricante,
# Fazer a ligação entre carro tem Motor
# Um motor pode ser de vários carros
# Fazer a ligação entre Carro e fabricante
# Um fabricante pode fabricar vários carros
# Exiba o nome do carro, fabricante e motor na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor    
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante

class Motor:
    def __init__(self, nome):
        self.nome=nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
motor_1_0 = Motor('1.0')
Volkswagen = Fabricante('Wolkswagen')
fusca.motor = motor_1_0
fusca.fabricante = Volkswagen
print(fusca.nome, fusca.motor.nome, fusca.fabricante.nome)