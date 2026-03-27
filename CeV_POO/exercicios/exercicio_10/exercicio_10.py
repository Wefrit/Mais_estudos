from rich.panel import Panel
from rich import print
from os import system

class ControleRemoto:
    def __init__(self):
        self.ligado = False
        self.botao = ''

        self.canais = [1, 2, 3, 4, 5]
        self.canal_atual_idx = 0

        self.volume_max = 5
        self.volume = 0

        self.texto = '[red]A TV está desligada[/red]'

        while True:
            system("cls")

            tv = Panel(
                title='[ TV ]',
                title_align='center',
                renderable=self.texto,
                expand=False
            )

            print(tv)
            print('< CH >   - VOL +')
            print('Botões: @ ligar/desligar | < canal- | > canal+ | - vol- | + vol+ | 0 sair')

            self.botao = input("Digite um botão: ").strip()

            if self.botao == "0":
                raise SystemExit

            self.ligar_desligar()
            self.mudar_canal()
            self.mudar_volume()
            self.atualizar_tela()

    # --------- helpers ---------
    def canais_formatados(self):
        partes = []
        for i, canal in enumerate(self.canais):
            if i == self.canal_atual_idx:
                partes.append(f"[black on yellow]{canal}[/black on yellow]")
            else:
                partes.append(str(canal))
        return " ".join(partes)

    def barra_volume(self):
        cheios = self.volume
        vazios = self.volume_max - self.volume
        return f"[green]{'█' * cheios}[/green]{'░' * vazios}"

    def atualizar_tela(self):
        if not self.ligado:
            self.texto = '[red]A TV está desligada[/red]'
            return

        self.texto = (
            f"CANAL = {self.canais_formatados()}\n"
            f"VOLUME = {self.barra_volume()}"
        )

    # --------- ações ---------
    def ligar_desligar(self):
        if self.botao != "@":
            return

        self.ligado = not self.ligado

    def mudar_canal(self):
        if not self.ligado:
            return

        if self.botao == ">":
            self.canal_atual_idx = (self.canal_atual_idx + 1) % len(self.canais)

        elif self.botao == "<":
            self.canal_atual_idx = (self.canal_atual_idx - 1) % len(self.canais)

    def mudar_volume(self):
        if not self.ligado:
            return

        if self.botao == "+" and self.volume < self.volume_max:
            self.volume += 1

        elif self.botao == "-" and self.volume > 0:
            self.volume -= 1


ControleRemoto()
