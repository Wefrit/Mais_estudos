from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, n_lados=0):
        self.n_lados = n_lados
    
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lados, n_lados=4):
        super().__init__(n_lados)
        self.lados = lados

    def perimetro(self):
        return self.lados * self.n_lados

    def area(self):
        return self.lados**2

class Circulo(Poligono):
    def __init__(self, raio, n_lados=0):
        super().__init__(n_lados)
        self.raio = raio
    
    def perimetro(self):
        PI = 3.14
        return 2* PI *self.raio

    def area(self):
        PI = 3.1415
        return PI * (self.raio**2)