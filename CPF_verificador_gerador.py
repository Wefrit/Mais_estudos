def verificador_de_cpf(cpf):
    digitos_multiplicados = []

    # tratamento de erros
    if not cpf.isdigit():
        raise ValueError('Digite apenas números')
    if len(cpf) != 11:
        raise ValueError('Digite 11 números')
    
    # calculando o primeiro dígito
    multiplicador_1 = 10
    for d in range (0,9):
        digitos_multiplicados.append(int(cpf[d]) * multiplicador_1)
        multiplicador_1 -= 1
    soma_digitos_multiplicados = sum(digitos_multiplicados)

    # verificando se o dígito é válido
    resultado = 0 if (soma_digitos_multiplicados * 10) % 11 > 9 else (soma_digitos_multiplicados * 10) % 11
    primeiro_digito = resultado

    # calculando o segundo digito
    digitos_multiplicados_2 = []
    multiplicador_2 = 11
    for d in range (0,10):
        digitos_multiplicados_2.append(int(cpf[d]) * multiplicador_2)
        multiplicador_2 -= 1
    soma_digitos_multiplicados_2 = sum(digitos_multiplicados_2)

    # verificando se o segundo digito é válido
    resultado = 0 if (soma_digitos_multiplicados_2 *10 ) % 11 > 9 else (soma_digitos_multiplicados_2 *10) % 11
    segundo_digito = resultado

    # verificando se o CPF é válido
    CPF_VALIDO = primeiro_digito == int(cpf[-2]) and segundo_digito == int(cpf[-1])
    if CPF_VALIDO:
        return 'CPF válido.'
    return 'CPF inválido.'


def gerador_de_cpf_valido(quantidade):
    import random

    lista_cpf = []
    # gera primeiros 9 numeros

    for _ in range(quantidade):
        cpf = ''
        for digito in range(9):
            cpf += str(random.randint(0,9))

        digitos_multiplicados = []

        multiplicador_1 = 10
        for d in range (0,9):
            digitos_multiplicados.append(int(cpf[d]) * multiplicador_1)
            multiplicador_1 -= 1
            soma_digitos_multiplicados = sum(digitos_multiplicados)

        resultado = 0 if (soma_digitos_multiplicados * 10) % 11 > 9 else (soma_digitos_multiplicados * 10) % 11
        primeiro_digito = resultado

        cpf += str(primeiro_digito)

        digitos_multiplicados_2 = []
        multiplicador_2 = 11
        for d in range (0,10):
            digitos_multiplicados_2.append(int(cpf[d]) * multiplicador_2)
            multiplicador_2 -= 1
            soma_digitos_multiplicados_2 = sum(digitos_multiplicados_2)

        # verificando se o segundo digito é válido
        resultado = 0 if (soma_digitos_multiplicados_2 *10 ) % 11 > 9 else (soma_digitos_multiplicados_2 *10) % 11
        segundo_digito = resultado

        cpf += str(segundo_digito)
        lista_cpf.append(cpf)

    return lista_cpf

def verificador_multiplo(lista_de_cpf):
    lista_cpfs_validos = []
    lista_cpfs_invalidos = []

    for item in lista_de_cpf:
        try:
            resultado = verificador_de_cpf(item)
            if resultado == 'CPF válido.':
                lista_cpfs_validos.append((item, resultado))
            else:
                lista_cpfs_invalidos.append((item, resultado))
        except ValueError as e:
            lista_cpfs_invalidos.append((item, f'Erro: {e}'))

    return lista_cpfs_validos, lista_cpfs_invalidos


