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

    return validacao


# teste_cpf = input("Digite o Cpf: ")
# print(cpf_validar(teste_cpf))

# verificação se cliente consta na "lista_clientes".
def eh_cliente(cpf):
    if str(cpf) in lista_clientes:
        return True
    else:
        return False


# cadastro cliente
# def novo_cliente(nome, cpf, senha):
#     nome = input("Digite seu nome: ").upper()
#     cpf = int(input("Digite seu CPF: "))
#     if str(cpf) in cadastro_clientes:
#         print("CPF já cadastrado.")
#     else:
#         if str(cpf) not in cadastro_clientes:
#             if cpf_validar(cpf) == True:
#                 while True:
#                     x = int(input("Crie uma senha de 4 números: "))
#                     y = int(input("Digite novamente sua senha para confirmar: "))
#                     if x == y:
#                         senha = x
#                         break
#             else:
#                 print("CPF inválido, tente novamente!")
#     cadastro_clientes.append(nome, cpf, senha)


# produtos disponíveis, quantidade e preço organizados em formato de dicionário
estoque_preco = [[1, "Pasta de dente", 12.0],
                 [2, "Feijão", 6.00],
                 [3, "Arroz", 4.50],
                 [4, "Macarrão", 3.75],
                 [5, "Bolacha", 4.80],
                 [6, "Leite", 2.90],
                 [7, "Shampoo", 14.75],
                 [8, "Detergente", 1.90],
                 [9, "Sabonete", 3.90],
                 [10, "Sabão em pó", 16.20]]

# cadastros existentes
lista_clientes = list()
cadastro = dict()

# menu
while True:
    print()
    print("Seja bem-vindo(a) a AmazonCC!")
    menu = int(input("""
    1 - Cadastro
    2 - Comprar
    3 - Mostrar carrinho
    4 - Pagar conta
    5 - Consultar Cliente
    6 - Mostrar produtos disponíveis
    0 - Sair\n"""))
    if menu == 0:
        break
    elif menu == 1:
        cpf = str(input("Digite seu Cpf: "))
        if cpf_validar(cpf) == True:
            cadastro["cpf"] = cpf
            cadastro["nome"] = input("Digite seu nome: ").upper()
            cadastro["e-mail"] = input("Digite seu melhor e-mail:").lower()
            cadastro["senha"] = int(input("Crie uma senha de 4 números:"))
            cadastro["limite"] = 1000.00
            lista_clientes.append(cadastro.copy())
    elif menu == 6:
        print(f"{'LISTA DE PRODUTOS DISPONÍVEIS':>33}")
        print("=-=" * 13)
        for item in estoque_preco:
            print(f"Cód. {item[0]:<3} {item[1]:.<20} r${item[2]:6.2f}")
        print("=-=" * 13)

# print(lista_clientes)
