class Empresa:
    def __init__(self, nome):
        self.nome = nome

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self._empresa = None

    @property
    def empresa(self):
        return self._empresa
    
    @empresa.setter
    def empresa(self, empresa):
        self._empresa = empresa

    def apresentacao(self):
        return f'Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa.nome}'
    


f1 = Funcionario('Maria', 'Administração', 'Diretora')
e1 = Empresa('Curso em  Vídeo')
f1.empresa = e1
print(f1.apresentacao())


