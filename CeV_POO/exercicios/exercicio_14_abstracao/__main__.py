from calculo_frete import *
from rich.table import Table
from rich import print
def main():
    dist = 8
    viagem = [Moto(dist), Caminhão(dist), Drone(dist)]
    tabela = Transporte.tabela(dist, viagem)
    print (tabela)


if __name__ == "__main__":
    main()