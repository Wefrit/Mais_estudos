class Caneta:
    def __init__(self, cor, nome):
        self._cor = cor
        self.nome = nome

    @property
    def cor(self):  
        return self._cor
    
    @cor.setter
    def cor(self,valor):
        self._cor = valor
    
    @classmethod
    def caneta_nome_joao(cls, cor):
        return cls(cor, 'João')

    @property
    def get_att(self):
        return self.nome, self._cor

caneta = Caneta('Azul', 'Carlos')
caneta_joao = Caneta.caneta_nome_joao('Preta')
print(caneta.cor)
caneta.cor = 'Rosa'
print(caneta.cor, caneta.nome)
print(caneta_joao.nome, caneta_joao.cor)
caneta_joao.cor = 'Azul'
print(caneta_joao.get_att)
print(caneta.get_att)