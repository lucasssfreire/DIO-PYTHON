menu = """

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

    opcao = (input(menu))

    if opcao == "1":
        valor = float(input("informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else:
            print("Ocooreu uma falha! voce informou um numero invalido, por favor tente novamente")

    elif opcao == "2":
        valor = float(input("Informe o valor de saque; "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Ocorreu uma falha! voce nao possui saldo suficiente, por favor tente novamente")

        elif excedeu_limite:
            print("Ocorreu uma falha! o valor excedeu o limite")

        elif excedeu_saques:
                    print("Ocorreu uma falha! numero de saques diarios excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Ocorreu uma falha! o valor informado é invalido")

    elif opcao == "3":
        print("\n---------- EXTRATO ----------")
        print("Nao foram relizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------")

    elif opcao == "4":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a opcao desejada")