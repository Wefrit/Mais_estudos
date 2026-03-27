# Declaração da classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos da Instância
        self.nome = ''
        self.idade = 0

    # Métodos da Instância
    def aniversario(self):
        self.idade += 1
        return self.idade
    
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'
    
# Declração de Objetos
g1 = Gafanhoto()
g1.nome = 'Clara'
g1.idade = 20

g1.aniversario()

print(g1.mensagem())