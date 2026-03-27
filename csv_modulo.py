import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csv_modulo.csv'

lista_clientes = [
    {'Nome': 'Surio', 'Idade': 42, 'Endereço': 'Rua, 22'},

]

 
with open(CAMINHO_CSV, 'a') as arquivo:
    colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=colunas
    )
    
    for cliente in lista_clientes:
        escritor.writerow(cliente)