lista = []
linhas = '-'*20

while True:
    opcao = input('\nSeleciona uma opção\n [i]nserir, [a]pagar, [l]istar, [s]air\n')
    
    # opção inserir
    if opcao == 'i':
        novo_item = input('\nO que você deseja inserir?\n')
        lista.append(novo_item)
        print(f'{novo_item.upper()} adicionado à lista')
        continue
    
    # opcao apagar
    if opcao == 'a':
        if lista == []:
            print('\n Nada para listar\n')
            continue
        # lista com itens
        else:
            for item in enumerate(lista):
                print(item[0]+1,'\t', item[1])
                while True:
                    try:
                        item = int(input('\nDigite o número do item que deseja apagar:\n'))
                        print(f'Item {lista[item-1]} excluído.\n')
                        lista.pop(item-1)
                        break
                    except:
                        print('Digite um número válido.')
                        continue
        continue   

    # opção listar
    if opcao == 'l':
        # lista vazia
        if lista == []:
            print('Nada para listar')
            continue
        # lista com itens
        else:
            for item in enumerate(lista):
                print(item[0]+1,'\t', item[1])
        continue

    # sai do programa
    if opcao == 's':
        break