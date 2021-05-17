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
def eh_cliente(cpf, lista):
    for k in lista:
        for valor in k:
            if str(valor) == str(cpf):
                return True
            else:
                return False


def pega_preco(indice_produto):
    for x in estoque_preco:
        if indice_produto == x[0]:
            return x[2]


def pega_nome_produto(indice_produto):
    for x in estoque_preco:
        if indice_produto == x[0]:
            return x[1]


def retorna_limite_cliente(cpf):
    for x in lista_clientes:
        for cliente in x:
            if x[0] == cpf:
                return x[4]


def atualiza_limite_cliente_pos_compras(cpf):
    for x in lista_clientes:
        for cliente in x:
            if x[0] == cpf:
                x[4] = retorna_limite_cliente(cpf) - soma_total
                return x[4]


def conta_a_pagar(cpf):
    for x in lista_clientes:
        for cliente in x:
            if x[0] == cpf:
                conta = x[4] - 1000.00
                return conta


def paga_conta(cpf):
    for x in lista_clientes:
        for cliente in x:
            if x[0] == cpf:
                x[4] += pagar
                return x[4]


def consultar_cliente(cpf):
    for x in lista_clientes:
        if x[0] == cpf:
            print(f"Nome do cliente: {x[1]}\nE-mail: {x[2]}")


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
estoque_preco = [[0, "Arroz", 7.00],
                 [1, "Pasta de dente", 12.0],
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
lista_clientes = [["06164351936", "Clarine", "cc@company.com", 3333, 1000.00],
                  ["05436556957", "Tiago", "tt@company.com", 4444, 2000.00]]
carrinho_compra = []

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
    elif menu == 1:  # cadastro
        cpf = str(input("Digite seu Cpf: "))
        if cpf_validar(cpf) == True:
            nome = input("Digite seu nome: ").upper()
            email = input("Digite seu melhor e-mail:").lower()
            senha = int(input("Crie uma senha de 4 números:"))
            limite = 1000.00
            lista_clientes.append((cpf, nome, email, senha, limite))
            print("Cadastro efetuado com sucesso")
            print()
        else:
            print("Número de Cpf inválido!")
        print(lista_clientes)
    elif menu == 2:  # comprar
        cpf = input("Digite seu Cpf: ")
        if eh_cliente(cpf, lista_clientes) == True:
            while True:
                id = int(input("Digite o código do produto.\nOu \"-1\" para fechar o carrinho:"))
                if id == -1:
                    break
                elif id < 0 or id > len(estoque_preco):
                    print("Opção inválida ou código não consta disponível em lista de produtos!!!")
                    continue
                indice_id = id
                qtd = int(input(f"Quantidade de {estoque_preco[indice_id][1]} que deseja comprar?"))
                carrinho_compra.append([indice_id, qtd])
                print(carrinho_compra)
        else:
            print("Cpf não encontrado, realize seu cadastro.")
    elif menu == 3:
        print(f"{'SEU CARRINHO DE COMPRAS':>33}")
        print("=-=" * 18)
        print(f"{'Produtos':>15}          {'Quantidade':^10}    {'Soma Parcial':^10}")
        print()
        soma_total = 0
        for item in carrinho_compra:
            preco_item = pega_preco(item[0])
            nome_item = pega_nome_produto(item[0])
            soma_itens = preco_item * item[1]
            soma_total += preco_item * item[1]
            print(f"{nome_item:>15}    x    {item[1]:^10}      R${soma_itens:6.2f}")
        print()
        print(f"Valor total do carrinho:                R${soma_total:6.2f}")
        print()
        print(f"Limite disponível para compra: R$ {retorna_limite_cliente(cpf) - soma_total:6.2f}")
        print("=-=" * 18)
        atualiza_limite_cliente_pos_compras(cpf)
    elif menu == 4:
        print(f"Valor da sua conta atual: {conta_a_pagar(cpf):6.2f} ")
        pagar = float(input("Qual valor que deseja pagar de sua conta atual: "))
        paga_conta(cpf)
        print("=-=" * 18)
        print()
        print(
            f"Seu limite atualizado é de R${retorna_limite_cliente(cpf):6.2f}\nNo momento sua conta a pagar é de R${conta_a_pagar(cpf):6.2f}")
        print()
        print("=-=" * 18)
    elif menu == 5:
        cpf = input("Digite o Cpf que deseja consultar: ")
        consultar_cliente(cpf)

    elif menu == 6:
        print(f"{'LISTA DE PRODUTOS DISPONÍVEIS':>33}")
        print("=-=" * 13)
        for item in estoque_preco:
            print(f"Cód. {item[0]:<3} {item[1]:.<20} R${item[2]:6.2f}")
        print("=-=" * 13)

# print(lista_clientes)
print(carrinho_compra)
print(lista_clientes)
