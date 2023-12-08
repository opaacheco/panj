
def sacar(valor, saldo, extrato, numero_saques, limite_saques, limite, /):
    if numero_saques>limite_saques:
        print("você ultrapassou o limite de saques!\n")
        return valor, extrato, numero_saques
    if valor > limite:
        print("você ultrapassou o seu limite!\n")
        return valor, extrato, numero_saques
    saldo -= valor
    print(f"Saque de R${valor:.2f} realizado.\n")
    extrato += f"Saque de R${valor:.2f}\n"
    numero_saques += 1
    return saldo, extrato, numero_saques

def depositar(valor="valor", extrato="extrato", saldo="saldo"):
    print("depositando", end="...\n")
    saldo += valor
    extrato += f"deposito de R${valor:.2f}\n"
    return extrato, saldo
    
def mostrar_extrato(extrato):
    print("======EXTRATO BANCARIO=====\n")
    print(" não tem transações ainda\n" if not extrato else extrato)
    print("===========================")    

def criar_cliente(pessoas):
    print("me informe esses dados por favor: ")
    cpf = input("cpf: ")
    pessoa = filtrar_usuario(cpf, pessoas)
    if pessoa:
        print("cliente ja cadastrado")
    cidade = input("cidade: ")
    nome = input("nome: ")
    pessoas.update({nome:{"nome":nome, "cpf":cpf, "cidade":cidade}})
    return pessoas
    
def filtrar_usuario(cpf, pessoas):
    # usuario_filtrado = [pessoa for chave, pessoa in pessoas if pessoa["cpf"] == cpf]
    # return usuario_filtrado[0] if usuario_filtrado else None
    for chave, pessoa in pessoas.items():
        if pessoa["cpf"] == cpf:
            return pessoa
    return None

def criar_conta(agencia, numero_conta, pessoas):
    print("me informe esses dados por favor: ")
    cpf = input("cpf: ")
    usuario = filtrar_usuario(cpf, pessoas)
    if usuario:
        print("conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "pessoa": usuario}
    return None

def listar_contas(contas):
    for conta in contas:
        text = f"""
        Agência = {conta["agencia"]}
        numero_conta = {conta["numero_conta"]}
        titular = {conta["pessoa"]["nome"]}
        """
        print(text)
    

def main():
    pessoas = {}
    contas = []
    
    menu = "\nescolha uma opção: \n[1] Sacar\n[2] Depositar\n[3] Extrato\n[4] Criar Cliente\n[5] Criar Conta\n[6] Listar Contas\n[0] Sair\n"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001" 

    while True : 
        
        opcao = int(input(menu))
        if opcao == 1:
            valor = int(input("\nvalor que deseja sacar:\n"))
            saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
        elif opcao == 2:
            valor = 0
            while valor <= 0 :
                valor = int(input("qual o valor deseja depositar:\n"))
            extrato, saldo = depositar(valor=valor, extrato=extrato, saldo=saldo)
        elif opcao == 3:
            mostrar_extrato(extrato)
        elif opcao == 4:
            pessoas = criar_cliente(pessoas)
            print(pessoas)
        elif opcao == 5:
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, pessoas)
            if conta:
                contas.append(conta)
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 0:
            break
        else:
            print("opção inválida")

main()