from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preço')

tabela.add_column('Poduto', justify='left', style='red')
tabela.add_column('Preço', justify='center')
tabela.add_column('Descrição', justify='right', style='blue')
tabela.add_row('Lápis comum', 'R$ 1.50', 'LAPIS COMUM')
tabela.add_row('Lápis incomum', 'R$ 3.00', 'LAPIS INCOMUM')
tabela.add_row('Lápis raro', 'R$ 9.00', 'LAPIS RARO')


print(tabela)