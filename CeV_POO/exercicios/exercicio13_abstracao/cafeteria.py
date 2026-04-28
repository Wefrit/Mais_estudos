from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print('--- Iniciando o Preparo ---')
        print('1. Fervendo a água a 100 graus Celsius.')
        self.misturar()
    
    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Passando água pressurizada pelo café moído.")
        self.servir()

    def servir(self):
        print ("3. Servindo em xícara pequena.")
        print('--- Bebida pronta ---')

class Chá(BebidaQuente):
    def misturar(self):
        print("2. Passando o sachê de ervas na água.")
        self.servir()

    def servir(self):
        print ("3. Servindo na caneca de porcelana com limão.")
        print('--- Bebida pronta ---')

class Leite(BebidaQuente):
    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")
        self.servir()

    def servir(self):
        print ("3. Servindo na caneca grande, ja com café.")
        print('--- Bebida pronta ---')