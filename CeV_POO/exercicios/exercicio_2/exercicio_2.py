# Declaração da classe
class Gafanhoto:
    '''
    Essa classe cria um Gafanhoto, que é uma pessoa com nome e idade.

    Para criar uma nova pessoa use:
    Gafanhoto(nome:str, idade:int)
    '''
    def __init__(self, nome = '', idade = 0): # Método Construtor
        # Atributos da Instância
        self.nome = nome
        self.idade = idade

    # Métodos da Instância
    def aniversario(self):
        self.idade += 1
        print(f'Feliz aniversário {self.nome}!, mais um aninho de vida')
        return self.idade
    
    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'
  
    
# Declração de Objetos
g1 = Gafanhoto('Clara', 17)
g1.aniversario()
print(g1)
print()
g2 = Gafanhoto('Mauro', 10)
g2.aniversario()
print(g2)
print()
print(Gafanhoto.__doc__) # Documentação

print(g1.__dict__)
print(g2.__class__)