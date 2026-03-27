import os

palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')

    # impede de digitar mais de um caracter ou digitar nada
    if len(letra_digitada) > 1 or letra_digitada == '' == ' ':
        print('Digite apenas uma letra.')
        continue
    
    # soma o número de tentativas
    tentativas += 1

    # compara a letra que você digitou com a palavra, se tiver ele acrescenta na variável das letras que acertou
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    # cria a variável para a palavra completa aparecer
    palavra_formada = ''

    # usa cada letra da palavra secreta para ver se tem nas letras que ja foram acertadas
    for letra in palavra_secreta:
        # caso tenho ele acrescenta na variável da palavra formada
        if letra in letras_acertadas:
            palavra_formada += letra
        # se não tiver na letras acertadas ele coloca um * na posição da palavra
        else:
            palavra_formada += '*'
    # retorna a palavra que foi formada até o momento        
    print(palavra_formada)
    
    # compara a palavra formada com a palavra secreta, se for igual, limpa o código e termina o jogo
    if palavra_secreta == palavra_formada:
        os.system('cls')
        break
    continue 

print(f'Parabés, você só precisou de {tentativas} tentativas para acertar a palavra "{palavra_formada}"')