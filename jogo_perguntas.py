perguntas = [
{
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1','2','3','4'],
    'Resposta': '4',
},
{
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['20', '25', '30', '35'],
    'Resposta': '25',

},
{
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['3','5', '10', '7'],
    'Resposta': '5',
},
]

pontos = 0
for pergunta in perguntas:
    print(f'Pergunta: {pergunta['Pergunta']}\n')
    print('Opçções:')
    
    for i, opção in enumerate(pergunta['Opções']):
        print(f'{i+1}) {opção}')
    x = int(input('Escolha: '))
    
    if pergunta['Resposta'] == pergunta['Opções'][x-1]:
        print('Acertou.\n')
        pontos += 1
    else:
        print('Errou.\n')
        
print(f'Você fez {pontos} pontos.')
