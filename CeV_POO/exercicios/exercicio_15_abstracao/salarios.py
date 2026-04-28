from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
        self.sal_min = 1612
        self.inss = 0.075

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        salario_liquido = self.calc_sal()
        qtd_sm = self.salario / self.sal_min
        print(f'O salário de {self.nome} é de {salario_liquido} e corresponde a {qtd_sm:.2f} salários mínimos')

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        self.salario = self.valor_hora * self.horas_trab
        return self.salario - (self.salario * self.inss)
    
class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto
        return self.salario * (1 - self.inss)
