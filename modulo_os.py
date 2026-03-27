import os
caminho = os.path.join('/Users','Lopes','OneDrive','Área de Trabalho','faculdade')


# for pasta in os.listdir(caminho):
#     cada_pasta = os.path.join(caminho, pasta)
#     print(os.path.basename(cada_pasta))

#     if not os.path.isdir(cada_pasta):
#         continue
    
#     for arquivo in os.listdir(cada_pasta):
#         print('  ',arquivo)


# for root, dirs, files in os.walk(caminho):
#     print('Raíz:\n', root)
#     print()
#     for _dir in dirs:
#         print(f'Pasta dentro de {os.path.basename(root)}:\n', _dir)
#         print()
#     for _file in files:
#         print(f'Arquivo dentro de {os.path.basename(_dir)}:\n', _file)
#         print()

# tamanho = os.stat(caminho).st_size

# print(tamanho)

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')

print(DESKTOP)