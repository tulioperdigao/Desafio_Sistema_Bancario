menu = """
====================
  SISTEMA BANCÁRIO
====================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Sua opção -> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print('-' * 30)
        print(f"{'DEPÓSITO':^30}")
        print('-' * 30)
        depositar = float(input("Digite o valor que deseja depositar: "))
        if depositar < 0:
            print("Valor negativo, não foi possível depositar.")
        else:
            saldo += depositar
            extrato += f"R${depositar}\n"
            print("Depósito efetuado com sucesso!")
    
    elif opcao == 2:
        print('-' * 30)
        print(f"{'SAQUE':^30}")
        print('-' * 30)
        sacar = float(input("Digite o valor que deseja sacar: "))
        if sacar <= saldo:
            if sacar <= limite:
                if numero_saques < LIMITE_SAQUES:
                    saldo -= sacar
                    numero_saques += 1
                    extrato += f"-R${sacar:.2f}\n"
                    print("Valor sacado com sucesso!")
                    print(f"Número de saques no dia: {numero_saques}")
                else:
                    print("Não foi possível sacar. Limite de saques atingido.")
            else:
                print("Não foi possível sacar. Saque acima do valor limite: R$500,00.")
        else:
            print("Não foi possível sacar. Saldo insuficiente.")
    
    elif opcao == 3:
        print('-' * 30)
        print(f"{'EXTRATO':^30}")
        print('-' * 30)
        print(extrato)
        print(f"SALDO: R${saldo:.2f}")
    
    elif opcao == 4:
        break
    
    else:
        print("Opção INVÁLIDA! Por favor, selecione novamente a operação desejada.")
