menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ""
saques = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado")
        else:
            print("Saldo insuficiente.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = saques >= limite_saque

        if excedeu_saldo:
            print("Saldo insuficiente")
        elif excedeu_limite:
            print("O saque deve ser de no maximo R$500")
        elif excedeu_saques:
            print("Maximo de saques atingido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques += 1
        else:
            print("Valor invalido")

    elif opcao == "3":
        print("=====EXTRATO=====")
        if not extrato:
            print("Extrato em branco.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================")

    elif opcao == "4":
        break

    else:
        print("Operação invalida")