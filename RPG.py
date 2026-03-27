from abc import ABC, abstractmethod
from rich import print
from time import sleep
from rich.prompt import Prompt

class Character:
    def __init__(self, name):
        self.name = name
        self.mana = 0
        self.base_mana = 0
        self.hp = 0
        self.base_hp = 0
        self.xp = 0
        self.lvl = 1
        self.abilities = {
            '1': {'name': 'cantar', 'points': 0},
            '2': {'name': 'dançar', 'points': 0},
        }

        self.attributes = {
            '1': {'name': 'forca', 'points': 0},
            '2': {'name': 'carisma', 'points': 0},
        }
        self.att_points = 0
        self.ability_points = 0
        self.magic_points = 0
        self.quality_points = 0


    # Ganhar xp
    def gain_xp(self, amount: int):
        self.xp += amount
        if self.xp >= (self.lvl+1)*100:
            self._level_up()
    
    def _level_up(self):
        while self.xp >= (self.lvl+1)*100:
            self.xp -= (self.lvl+1)*100
            self.lvl += 1
            print(f'[green]^ LVL UP ^[/green]\nLVL {self.lvl}')
            self._receive_stats_points()
            self.spend_points()

    def use_magic(self):
        if self.mana > 0:
            if self.hp <= 0:
                print('Morto não usa magia.')
            else:
                self.mana -= 1
                print(f':star2:[blue]{self.mana}/{self.base_mana}[/]')
        else:
            print('Você não tem mana pra gastar')

    def use_mana_potion(self):
        if self.mana < self.base_mana:
            self.mana += 1
            print(f'{self.name} tomou 1 poção e recuperou 1 de mana\n [blue]HP: {self.mana}/{self.base_mana}[/]')
        else:
            print('Sua mana ja está cheia!')

    def take_damage(self,damage):
        if self.hp > 0:
            for _ in range(damage):
                self.hp -= 1
                print(f':knife: {self.hp}/{self.base_hp}')
                sleep(0.5)
                if self.hp <= 0:
                    print('Você morreu!:skull:')
                    break
        else:
            print('Você ja está sem vida!')

    def use_hp_potion(self):
        if self.hp < self.base_hp:
            self.hp += 1
            print(f'{self.name} tomou 1 poção e recuperou 1 de hp\n [red]HP: {self.hp}/{self.base_hp}[/]')
        else:
            print('Seu hp ja está cheio!')

    def display_stats(self):
        print(f'[black bold on bright_black]Player : {self.name} - LVL {self.lvl}[/]\n'
            f'[red]HP : {self.hp}/{self.base_hp}[/red]\n'
            f'[blue]Mana : {self.mana}/{self.base_mana}\n'
        )
    def display_points(self):
        print('habilidades:',f'{self.list_abilities()}\n',\
        'atributos:', f'{self.list_attributes()}\n',\
        f'qualidades:{self.quality_points}',\
        f'poder: {self.magic_points}',\
        f'XP: {self.xp}', sep='\n')

    def list_abilities(self):
        return '\n'.join([f'[blue]{k}[/blue] -> {v['name']} [green]{v['points']} pontos[/]' for k, v in self.abilities.items()])

    
    def list_attributes(self):
        return '\n'.join([f'[blue]{k}[/blue] -> {v['name']} [green]{v['points']} pontos[/]' for k, v in self.attributes.items()])

    def spend_points(self):
        while self.ability_points > 0:
            print(f'Pontos de habilidade: {self.ability_points}\n')
            choice = Prompt.ask(
                f'Em qual destas habilidade você gostaria de gastar:\n{self.list_abilities()} '
                ).strip()
            if choice in self.abilities:
                self.abilities[choice]['points'] += 1
                self.ability_points -= 1
                print(f'Você gastou 1 ponto em {self.abilities[choice]['name']}!')
            else:
                print('erro')
        while self.att_points > 0:
            print(f'Pontos de atributos: {self.att_points}\n')
            choice = Prompt.ask(
                f'Em qual destes atributos você gostaria de gastar:\n{self.list_attributes()} '
                ).strip()
            if choice in self.attributes:
                self.attributes[choice]['points'] += 1
                self.att_points -= 1
                print(f'Você gastou 1 ponto em {self.attributes[choice]['name']}!')
            else:
                print('erro')

class Job(Character, ABC):

    @abstractmethod
    def _receive_stats_points(self):
        ...

class Bardo(Job):
    def __init__(self, name):
        super().__init__(name)
        self.base_hp = 3
        self.base_mana = 3
        self.hp = 3
        self.mana = 3

    def _receive_stats_points(self):
        if self.lvl % 6 == 0:
            self.base_mana += 2
            print(f'Você ganhou +2 de mana!\n:right_arrow: Mana: {self.mana}/{self.base_mana}')
        if self.lvl % 5 == 0:
            self.att_points += 1
        if self.lvl % 4 == 0:
            self.magic_points += 1
            print(f'Você ganhou 1pt de poder! [yellow]Gaste em ficha[/]')
        if self.lvl % 3 == 0:
            self.quality_points += 2
            print(f'Você ganhou 2pt de qualidade![yellow]Gaste em ficha[/]')
        if self.lvl % 2 == 0:
            self.base_hp += 1
            print(f'Você ganhou +1 de hp!\n :right_arrow: HP: {self.hp}/{self.base_hp}')
        self.ability_points += 1




        

if __name__ == "__main__":
    
    
    bardo = Bardo('Jonatas')
    bardo.display_stats()
    bardo.gain_xp(250)
    bardo.display_points()

