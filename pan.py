menu = "escolha uma opção: \n[1] Sacar\n[2] Depositar\n[3] Extrato\n[0] Sair\n"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True : 
    
    opcao = int(input(menu))
    if opcao == 1:
        print(numero_saques)
        valor = int(input("valor que deseja sacar:\n"))
        if valor <= 0:
            print("não é possivel sacar esse valor", end="...\n")
        elif valor > limite:
            print("não é possivel sacar além do limite", end="...")
        elif valor > saldo:
            print("seu saldo é inferior ao montante pra sacar", end="...")
        else:
            saldo -= valor
            print(f"saque de R${valor} realizado", end="...")
            extrato += f"saque de R${valor:.2f}\n"
            numero_saques += 1
    elif opcao == 2:
        valor = 0
        while valor <= 0 :
            valor = int(input("qual o valor deseja depositar:\n"))
        print("depositando", end="...\n")
        saldo += valor
        extrato = f"deposito de R${valor:.2f}\n"
    elif opcao == 3:
        print("======EXTRATO BANCARIO=====\n")
        print(" não tem transações ainda\n" if not extrato else extrato)
        print("===========================")
    elif opcao == 0:
        break
    else:
        print("opção inválida")