import Contas

class Pessoa: 
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name}({attrs})'



class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Contas.Conta | None = None


if __name__ == '__main__':
    import Contas
    cliente_Luiz = Cliente('Luiz', 31)
    cliente_Luiz.conta = Contas.ContaPoupanca(123,222)
    cliente_Luiz.conta.depositar(50)
    print(cliente_Luiz, cliente_Luiz.conta)
    print(cliente_Luiz.conta)
