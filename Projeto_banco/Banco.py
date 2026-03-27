import Contas
import Pessoas

class Banco:
    def __init__(
            self, 
            agencias: list[int] | None = None,
            clientes: list[Pessoas.Pessoa] |None = None,
            contas: list[Contas.Conta] = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False
    
    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False
    
    def _checa_se_conta_e__do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e__do_cliente', True)
            return True
        print('_checa_se_conta_e__do_cliente', False)
        return False


    def autenticar(self, clientes: Pessoas.Pessoa, conta: Contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(clientes) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e__do_cliente(clientes, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencias!r}, {self.clientes!r},{self.contas!r}'
        return f'{class_name}({attrs})'

if __name__ == '__main__':
    c1 = Pessoas.Cliente('Luiz', 30)
    cc1 = Contas.ContaCorrente(111,222,0,0)
    c1.conta = cc1
    c2 = Pessoas.Cliente('Maria', 18)
    cp2 = Contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp2

    
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp2])
    banco.agencias.extend([111, 112])

    if banco.autenticar(c2, cp2):
        cc1.depositar(10)
        print(c1.conta)

    print(c2.conta)
