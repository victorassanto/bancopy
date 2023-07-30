import textwrap as tx


def exibir_menu():
    menu = """\n
    ================= Menu ===============
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNovo conta
    [6]\tListar contas
    [7]\tSair
    ======================================
    => """
    return input(tx.dedent(menu))


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Deposito realizado com sucesso!")
    else:
        print("Valor informado é inválido")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print('Saldo insuficiente para o saque.')

    elif numero_saques >= limite_saques:
        print('Limite diário de saques atingido.')

    elif valor > limite:
        print('Valor de saque excede o limite')

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Valor inválido!")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):

    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f'Saldo atual: R$ {saldo:.2f}')


def criar_usuario(usuarios):

    cpf = input('Digite o CPF do usuário (apenas números): ')

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome,
                     "data_nascimento": data_nascimento,
                     "cpf": cpf,
                     "endereco": endereco
                     })
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(" Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(tx.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = exibir_menu()

        if opcao == '1':
            valor = float(input('Digite o valor do depósito: '))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Digite o valor do saque: '))
            saldo, extrato = saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Por favor, selecione novamente.')
        print()


main()
