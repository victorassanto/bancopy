transacoes = []
saldo = 0
saques_diarios = 0
saques_registrados = []


def deposito(valor):
    global saldo
    if valor > 0:
        saldo += valor
        transacoes.append(f'Depósito: R$ {valor:.2f}')
        print(
            f'Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {saldo:.2f}')


def saque(valor):
    global saldo
    if saldo >= valor and saques_diarios < 3 and valor <= 500:
        saldo -= valor
        saques_diarios += 1
        transacoes.append(f'Saque: R$ {valor:.2f}')
        print(f'Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {saldo:.2f}')
    elif saldo < valor:
        print('Saldo insuficiente para o saque.')
    elif saques_diarios >= 3:
        print('Limite diário de saques atingido.')
    elif valor > 500:
        print('Limite máximo de R$ 500,00 por saque.')


def extrato():
    print('Extrato:')
    if not transacoes:
        print('Não foram realizadas movimentações.')
    else:
        for transacao in transacoes:
            print(transacao)
    print(f'Saldo atual: R$ {saldo:.2f}')

# Função para exibir o menu e realizar as interações


def exibir_menu():
    print('----- Menu -----')
    print('1. Realizar depósito')
    print('2. Realizar saque')
    print('3. Exibir extrato')
    print('4. Sair')
    print()


# Exemplo de uso das operações com o menu
saldo_inicial = float(input('Digite o saldo inicial: '))
saldo = saldo_inicial

while True:
    exibir_menu()
    opcao = input('Selecione uma opção: ')

    if opcao == '1':
        valor = float(input('Digite o valor do depósito: '))
        deposito(valor)
    elif opcao == '2':
        valor = float(input('Digite o valor do saque: '))
        saque(valor)
    elif opcao == '3':
        extrato()
    elif opcao == '4':
        print('Encerrando o programa...')
        break
    else:
        print('Opção inválida. Por favor, selecione novamente.')
    print()
