import re


# Função para validar CPF
def validar_cpf(cpf, usuarios):
    # Remover qualquer caractere não numérico
    cpf = re.sub(r'\D', '', cpf)

    # Verificar se o CPF já está cadastrado
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Operação falhou! Já existe um usuário com esse CPF.")
            return False
    return True


# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF (somente números): ")

    # Validando CPF
    if not validar_cpf(cpf, usuarios):
        return usuarios  # Retorna a lista sem alterações caso o CPF seja inválido

    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Criando um dicionário com os dados do usuário
    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
        'contas': []  # Lista de contas do usuário
    }

    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

    return usuarios


# Função para exibir todos os usuários cadastrados
def exibir_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"\nNome: {usuario['nome']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Endereço: {usuario['endereco']}")
            print("===================================")


# Função para cadastrar uma nova conta
def cadastrar_conta(usuarios, contas):
    cpf_usuario = input("Informe o CPF do usuário para cadastrar a conta: ")

    # Verificar se o CPF existe
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf_usuario:
            usuario = u
            break

    if not usuario:
        print("Usuário não encontrado.")
        return contas

    # Criar a conta
    numero_conta = len(contas) + 1  # Número da conta sequencial
    agencia = "0001"  # Agência fixa

    conta = {
        'agencia': agencia,
        'numero_conta': numero_conta,
        'usuario': usuario['nome']
    }

    # Adicionar a conta à lista de contas do usuário
    usuario['contas'].append(conta)
    contas.append(conta)
    print(f"Conta {numero_conta} criada para o usuário {usuario['nome']} com sucesso!")

    return contas


# Função para exibir todas as contas cadastradas
def exibir_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"\nAgência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Titular: {conta['usuario']}")
            print("===================================")


# Função para realizar o depósito
def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


# Função para realizar o saque
def sacar(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


# Função para exibir o extrato
def exibir_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def main():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar Usuário
    [l] Listar Usuários
    [c] Cadastrar Conta
    [x] Listar Contas
    [q] Sair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []  # Lista para armazenar os usuários cadastrados
    contas = []  # Lista para armazenar as contas

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(extrato, saldo)

        elif opcao == "u":
            usuarios = cadastrar_usuario(usuarios)

        elif opcao == "l":
            exibir_usuarios(usuarios)

        elif opcao == "c":
            contas = cadastrar_conta(usuarios, contas)

        elif opcao == "x":
            exibir_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
