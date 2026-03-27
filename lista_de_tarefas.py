import json


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa.')
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, excluidas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        return
    tarefa = tarefas.pop()
    excluidas.append(tarefa)
    print()

def refazer(excluidas, tarefas):
    print()
    if not excluidas:
        print('Nenhuma tarefa para refazer.')
        return
    excluida = excluidas.pop()
    tarefas.append(excluida)
    print()

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'tarefas.txt'
tarefas = ler([],CAMINHO_ARQUIVO)
excluidas = []

while True:
    nova_tarefa = str(input('Comando: listar, desfazer, refazer, sair. \n' \
    'Digite uma tarefa ou comando: '))

    if nova_tarefa == 'listar':
        listar(tarefas)

    elif nova_tarefa == 'desfazer':
        desfazer(tarefas, excluidas)
        salvar(tarefas, CAMINHO_ARQUIVO)

    elif nova_tarefa == 'refazer':
        refazer(excluidas,tarefas)
        salvar(tarefas, CAMINHO_ARQUIVO)

    elif nova_tarefa == 'sair':
        break

    else:
        tarefas.append(nova_tarefa)
        salvar(tarefas, CAMINHO_ARQUIVO)
        listar(tarefas)
