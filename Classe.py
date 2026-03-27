import json


CAMINHO_ARQUIVO = 'arquivo_classe.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade



p1 = Pessoa('João', 31)
p2 = Pessoa('Clara', 21)
p3 = Pessoa('Lizo', 14)
bd = [vars(p1),p2.__dict__,p3.__dict__]



with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
