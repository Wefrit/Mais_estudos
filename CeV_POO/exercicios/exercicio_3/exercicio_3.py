class ContaBancaria:
    '''
    Cria uma conta bancária que permite saques e depósitos
    '''
    def __init__(self, id: int, nome: str, saldo: int =0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso.\nTitular: {self.titular}\nSaldo: R${self.saldo:,.2f}')
    def __str__(self):
        return f'A conta {self.id}, do titular {self.titular} tem R${self.saldo:,.2f}'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Foi depositado R${valor:,.2f} na conta')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Você tentou sacar {valor:,.2f}. Valor de saque maior do que saldo na conta')
            print(f'Saldo disponível: R${self.saldo:,.2f}')
        else:
            self.saldo -= valor
            print(f'Você sacou R${valor}')
            print(f'Saldo disponível: R${self.saldo:,.2f}')

c1 = ContaBancaria(112, 'Gustavo', 3000)
c1.depositar(500)
c1.sacar(35000000000)
print(c1)