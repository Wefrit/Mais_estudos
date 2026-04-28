from abc import ABC, abstractmethod
from rich.table import Table

class Transporte(ABC):
    def __init__(self, distancia, fator):
        self.distancia = distancia
        self.fator = fator

    @abstractmethod
    def calc_frete(self):
        pass
    
    def tabela(dist, tipos):
        tabela_frete = Table(title='Tabela de Frete')
        tabela_frete.add_column('Distância')
        tabela_frete.add_column('Tipo')
        tabela_frete.add_column('Frete')

        for tipo in tipos:
            tabela_frete.add_row(f'{dist}',f'{type(tipo).__name__}',tipo.calc_frete())
        return tabela_frete
    
class Moto(Transporte):
    def __init__(self, distancia, fator=0.5):
        super().__init__(distancia, fator)

    def calc_frete(self):
        return f"R$ {self.distancia * self.fator}"

class Caminhão(Transporte):
    def __init__(self, distancia, fator=1.2):
        super().__init__(distancia, fator)

    def calc_frete(self):
        if self.distancia < 50:
            return 'Distância mínima para frete de 50 km.'
             
        else:
            return f"R$ {self.distancia * self.fator}"

class Drone(Transporte):
    def __init__(self, distancia, fator=9.5):
        super().__init__(distancia, fator)

    def calc_frete(self):
        if self.distancia > 10:
            return 'Distância máxima de 10 km.'
        else:
            return f"R$ {self.distancia * self.fator}"
