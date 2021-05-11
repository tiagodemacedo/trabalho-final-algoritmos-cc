# validação CPF
def cpf_validar(param1):
    cpf_string = str(param1)
    digitos9 = cpf_string[:-2]
    contador = 10
    contador_2 = 11
    soma = 0

    for x in digitos9:
        x = int(x)
        soma += x * contador
        contador -= 1
    resto_divisao = soma % 11

    digitos10 = None

    if resto_divisao < 2:
        digitos10 = digitos9 + "0"
    else:
        digitos10 = digitos9 + str(11 - resto_divisao)

    soma = 0
    digitos11 = None

    for x in digitos10:
        x = int(x)
        soma += x * contador_2
        contador_2 -= 1
    resto_divisao = soma % 11

    if resto_divisao < 2:
        digitos11 = digitos10 + "0"
    else:
        digitos11 = digitos10 + str(11 - resto_divisao)

    copia_digito11 = list(digitos11)
    copia_cpf_string = list(cpf_string)

    validacao = False

    if copia_digito11[9] == copia_cpf_string[9] and copia_digito11[10] == copia_cpf_string[10]:
        validacao = True
    else:
        validacao

    return validacao


cpf = input("Digite o Cpf: ")
print(cpf_validar(cpf))

# cadastro cliente

# senha cliente

# produtos disponíveis, quantidade e preço organizados em formato de dicionário

estoque = {"1 - Pasta de dente", 1000, 12.00,
           "2 - Feijão", 1000, 6.00,
           "3 - Arroz", 1000, 4.50,
           "4 - Macarrão", 1000, 3.75,
           "5 - Bolacha", 1000, 4.80,
           "6 - Leite", 1000, 2.90,
           "7 - Shampoo", 1000, 14.75,
           "8 - Detergente", 1000, 1.90,
           "9 - Sabonete", 1000, 3.90,
           "10 - Sabão em pó", 1000, 16.20}

# print(estoque)
