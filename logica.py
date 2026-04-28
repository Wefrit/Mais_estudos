# 1 - Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.

def soma():
    a, b, c = int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite o ultimo valor: '))
    soma_a_b = a+b
    print(f'A soma de {a} + {b} é igual {soma_a_b}')    
    if c > soma_a_b:
        print(f'{c} é maior que {a} + {b}')
    else:
        print(f'{c} não é maior que {a} + {b}')


# 2 - Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.
def classifica_numero():
    x = int(input('Digite um valor: '))
    if x > 0:
        if x % 2 == 0:
            print(f'{x} é positivo e par')
        else:
            print(f'{x} é positivo e ímpar')
    elif x < 0:
        if x % 2 == 0:
            print(f'{x} é negativo e par')
        else:
            print(f'{x} é negativo e ímpar')
    else:
        print('0 n vale')
# 3 - Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores, 
# caso contrário devera multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma variável C e
# imprimir seu valor na tela.

def soma_ou_multiplica():
    a,b = int(input('Digite um valor: ')), int(input('Digite outro valor: '))
    if a == b:
        soma = a+b
        print(f' o resultadot de {a}+{b} é {soma}')
    else:
        multiplica = a * b
        print(f'o resultado de {a} x {b} é {multiplica}')

# 4 - Faça um algoritmo que receba um número inteiro e imprima na tela o seu antecessor e o seu sucessor.
def antes_depois():
    x = int(input('Digite um valor: '))
    print(f'O número {x} vem depois de {x-1} e antes de {x+1}')


# 5 - Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse 
# usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).

def qts_sm():
    sm = 1293.20
    x = int(input('Digite um valor: '))
    print(f'O seu salário é o equivalente à {x/sm:.2f} do salário mínimo')


# 6 - Faça um algoritmo que leia um valor qualquer e imprima na tela com um reajuste de 5%.
def reajuste_5():
    x = int(input('Digite um valor: '))
    print(f'O valor informado está entre {x - (x*0.05)} e {x + (x*0.05)}')

# 7 - Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO.
def valores_booleanos():
    x, y= str(input('Digite um valor(V/F): ')), str(input('Digite um valor(V/F): '))

    if x == y:
        return print(True)
    return print(False)

# 8 - Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.
def imprime_dec():
    ns = []
    x,y,z = int(input('Digite um valor: ')), int(input('Digite outro valor: ')),int(input('Digite mais um valor: '))
    ns.append(x)
    ns.append(y)
    ns.append(z)
    print(sorted(ns, reverse=True))


# 9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 
# de acordo com a tabela abaixo:
# Fórmula do IMC = peso / (altura) ²
# Tabela Condições IMC
#  Abaixo de 18,5   | Abaixo do peso          
#  Entre 18,6 e 24,9 | Peso ideal (parabéns)  
#  Entre 25,0 e 29,9 | Levemente acima do peso
#  Entre 30,0 e 34,9 | Obesidade grau I 
#  Entre 35,0 e 39,9 | Obesidade grau II (severa)
#  Maior ou igual a 40 | Obesidade grau III (mórbida)

def IMC():
    x, y = int(input('Digite seu peso: ')), float(input('Digite sua altura(em metros): '))
    imc = x / (y**2)
    print(imc)
    if imc <= 18.5:
        print('Abaixo do peso')
    elif imc < 24.9:
        print('Peso ideal')
    elif imc < 29.9:
        print('Levemente acima do peso')
    elif imc < 34.9:
        print('Obesidade I')
    elif imc < 39.9:
        print('Obesidade II')
    else:
        print('Obesidade III')


#  10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.
def media():
    x,y,z = float(input('Digita a primeira nota: ')), float(input('Digita a segunda nota: ')),  float(input('Digita a terceira nota: '))
    media = (x + y + z) / 3
    print(f'A média é de {media:.2f}')


#  11 - Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno e 
#  se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.
def aprovado():
    a,b,c,d = float(input('Digite a nota do primeiro bimestre: ')),float(input('Digite a nota do segundo bimestre: ')),\
    float(input('Digite a nota do terceiro bimestre: ')), float(input('Digite a nota do quarto bimestre: '))
    media = (a+b+c+d)/4
    aprovado = media >= 7
    if aprovado:
        print(f'A média é de {media:.2f}. Aprovado')
    else:
        print(f'A média é de {media:.2f}. Reprovado')

#  12 - Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento
#  pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.
#  Tabela de Código de Condições de Pagamento
#  1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
#  2 - À Vista no cartão de crédito, recebe 10% de desconto
#  3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
#  4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%
def forma_pagamento():
    valor = float(input('Valor do produto: R$'))
    formas = int(input('Qual forma deseja efetuar o pagamento:\n' \
    '[1] À vista no dinheiro ou pix (15% de desconto)\n' \
    '[2] À vista no crédito (10% de desconto)\n'\
    '[3] Parceçadp 2x sem juros\n'\
    '[4] Parcelado 3x ou mais juros de 10%): '))
    if formas == 1:
        print(f'Valor total:{valor - (valor*0.15)}'),
    elif formas == 2:
        print(f'Valor total:{valor - (valor*0.10)}'),
    elif formas == 3:
        print(f'Valor total:{valor}'),
    else:
        print(f'Valor total:{valor + (valor*0.10)}'),



#  13 - Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 
def maior_idade():
    nome, idade, peso= str(input('Digite seu nome: ')), int(input('Digite sua idade: ')), float(input('Digita eu peso: '))
    if idade < 18:
        print(f'{nome} tem {idade} anos, então é menor de idade')
    else:
        print(f'{nome} tem {idade} anos, então é maior de idade')


# 14 - Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.
def troca_valor():
    valores = []
    a,b = int(input('Digite o valor de A: ')), int(input('Digite o valor de B: '))
    valores.append(a)
    valores.append(b)
    a = valores[1]
    b = valores[0]
    print(f' A vale {a} e B vale {b}')


# 15 - Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em 
# consideração o ano com 365 dias e o mês com 30 dias.
# (Ex: 5 anos, 2 meses e 15 dias de vida)
def idade_absoluta():
    from datetime import date
    data = str(input('Digite sua data de nascimento(DD-MM-AAAA): '))
    dia_str, mes_str, ano_str = data.split('-')
    dia = int(dia_str)
    mes = int(mes_str)
    ano = int(ano_str)
    nascimento = date(ano, mes, dia)
    hoje = date.today()
    anos = hoje.year - nascimento.year
    meses = hoje.month - nascimento.month
    dias = hoje.day - nascimento.day
    if dias < 0:
        meses -= 1
        if hoje.month == 1:
            dias += 31
        else:
            dias += (date(hoje.year, hoje.month, 1) - date(hoje.year, hoje.month - 1, 1)).days
    if meses < 0:
        anos -= 1
        meses += 12
    print(f'{anos} anos, {meses} meses e {dias} dias')


# 16 - Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos, determine se o triângulo é 
# equilátero, isósceles ou escaleno.

# 17 - Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

# Fórmula: C = (5 * ( F-32) / 9)

# 18 - Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano. Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Francisco seja maior que Sara.

# 19 - Faça um algoritmo que imprima na tela a tabuada de 1 até 10.

# 20 - Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

# 21 - Faça um algoritmo que mostre um valor aleatório entre 0 e 100.

# 22 - Faça um algoritmo que leia dois valores inteiros A e B, imprima na tela o quociente e o resto da divisão inteira entre eles.

# 21 - Faça um algoritmo que efetue o cálculo do salário líquido de um professor. As informações fornecidas serão: valor da hora aula, número de aulas lecionadas no mês e percentual de desconto do INSS. Imprima na tela o salário líquido final.

# 22 - Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, sabendo que o carro faz 12km com um litro. Deve-se fornecer ao usuário o tempo que será gasto na viagem a sua velocidade média, distância percorrida e a quantidade de litros utilizados para fazer a viagem.

# Fórmula: distância = tempo x velocidade.

#             litros usados = distância / 12.