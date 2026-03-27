"""
Exercício com Abstração, Heranla, Encapsulamento e Polimorfismo. 
Criar um sistema bancário (extremamente simples) que tenha clientes, contas e um banco. A idéia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacara/depositar nessa conta. Contas correntes tem um limite extra.

Conta(ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta

Banco 
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa(Herança)//////
    Pessoa tem nome e idade(com getter) //////
    Cliente TEM conta (Agregação da classse ContaCorrente ou Conta Poupança)///
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter métodos para depósito
    Conta (super classe) deve ter o método sacar abstrato(Abstração e////////
    polimorfimos - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contar(Agregação)
Banco será responsável por autenticar o cliente e as contas da seguinte forma:
    Banco tem contas e clientes(Agregação)
    * Checar se a agencia é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco(descrita acima)
Banco autentica por um método
"""


from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, conta: int , saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor: float) -> float:...

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        print(f'Depositado R${valor}')
        self.detalhes()

    def detalhes(self, msg: str ='') -> None:
        print(f'O seu saldo é R${self.saldo:.2f}{msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia!r},{self.conta!r}, {self.saldo!r}'
        return f'{class_name}({attrs})'

class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Saque de R${valor}') 
            return self.saldo
        
        print('Não foi possível sacar o valor informado')
        self.detalhes(f'SAQUE NEGADO:  R${valor}')


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'Saque de R${valor}') 
            return self.saldo
        
        print('Não foi possível sacar o valor informado')
        print(f'Seu limite é R${self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO:  R${valor}')
    
        def __repr__(self):
            class_name = type(self).__name__
            attrs = f'{self.agencia!r},{self.conta!r}, {self.saldo!r}, {self.limite!r}'
            return f'{class_name}({attrs})'


if __name__ == '__main__':
    cp1 = ContaCorrente(5555, 2222, 35, 50)
    cp1.depositar(1)
    cp1.sacar(86)
    cp1.sacar(1)
    print(cp1.saldo)
