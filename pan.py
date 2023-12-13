from abc import ABC, ABCMeta, abstractclassmethod, abstractproperty

from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
         self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo or 0
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def histoirco(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n@@@ operação falhou! você não tem saldo suficiente. @@@")
        
        elif not excedeu_saldo and valor > 0:
            self._saldo -= valor
            print("\n@@@ operação realizada com sucesso! @@@")
            return True
        else:
            print("\n@@@ operação falhou! valor inválido. @@@")

        return False
        
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n=== Operação falhou, valor inválido! ===")
            return False

        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_de_saques = len([transacao for transacao in self._historico.transacao if transacao["tipo"] == Saque])
        excedeu_limite = valor > self._limite 
        excedeu_saques = numero_de_saques > self._limite_saques
        
        if excedeu_limite:
            print("\n@@@ operação falhou! você não tem limite o suficiente! @@@")
        
        elif excedeu_saques:
             print("\n@@@ operação falhou! você não tem mais saques disponiveis! @@@")
        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"{self.__class__.__name__} : {", ".join([f"{key} = {value}" for key,value in self.__dict__.items()])}"

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strtime("%d-%m-%Y %H:%M:%s")
            }
        )

class Transacao(ABC):
    
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @classmethod
    def registrar(conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
class Depositar(Transacao):
        def __init__(self, valor):
            self._valor = valor

        @property
        def valor(self):
            return self._valor
        
        def registrar(self, conta):
            sucesso_transacao = conta.depositar(self.valor)
            
            if sucesso_transacao:
                conta.historico.adicionar_transacao(self)

def menu():
    menu = "\nescolha uma opção: \n[1] Sacar\n[2] Depositar\n[3] Extrato\n[4] Criar Cliente\n[5] Criar Conta\n[6] Listar Contas\n[0] Sair\n"
    return int(input(menu))

def sacar(clientes):
    cliente = credencial_cliente(clientes, "cliente não existe!!!")
    valor = float(input("informe o valor do saque : "))
    
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)    
    
def credencial_cliente(clientes, mensagem):    
    cpf = input("informe o cpf do cliente : ")
    cliente = filtrar_usuario(cpf, clientes)
    
    if not cliente:
        print(mensagem)
        return

def depositar(clientes):
    cliente = credencial_cliente(clientes, "cliente não existe!!!")
    
    if not cliente:
        print("cliente não encontrado!!!")
        return
    
    valor = float(input("informe o valor do deposito : "))
    
    transacao = Depositar(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)
    
def mostrar_extrato(clientes):
    cliente = credencial_cliente(clientes)
    conta = recuperar_conta_cliente(cliente)
    print("======EXTRATO BANCARIO=====\n")
    transacoes = conta.hisorico.transacoes
    
    extrato = " "
    if not transacoes:
        print("ainda não possui movimentações na conta!")
    else:
        for transacao in transacoes:
            extrato = f"\ntipo : {transacao['tipo']} - valor : R${transacao['valor']:.2f} - data : {transacao['data']}"  
    print(extrato)
    print(f"saldo da conta de R${conta.saldo}")
    print("===========================")    

def criar_cliente(clientes):
    cpf = input("informe o cpf do cliente : ")
    cliente = filtrar_usuario(cpf, clientes)
    
    if not cliente:
        print("cliente ja registrado!!!")
        return
    
    nome = input("informe o nome completo : ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa) : ")    
    endereco = input("informe o endereço : ")
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, endereco=endereco, cpf=cpf)
    
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("esse cliente não possui conta!!!")
        return
    
def filtrar_usuario(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(numero_contas, clientes, contas):
    cliente = credencial_cliente(clientes)
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_contas)

    contas.append(conta)
    cliente.contas.append(conta)

    print("conta criada com sucesso!!!")
    
    # if usuario:
    #     print("conta criada com sucesso!")
    #     return {"agencia": agencia, "numero_conta": numero_conta, "pessoa": usuario}
    # return None

def listar_contas(contas):
    for conta in contas:
       print("=" * 100)
       print(str(conta))
       
def main():
    pessoas = []
    contas = []
    
    while True : 
        
        opcao = menu()
        
        if opcao == 1:
            depositar(pessoas)
        elif opcao == 2:
            sacar(pessoas)
        elif opcao == 3:
            mostrar_extrato(pessoas)
        elif opcao == 4:
            pessoas = criar_cliente(pessoas)
            print(pessoas)
        elif opcao == 5:
            numero_conta = len(contas)+1
            criar_conta(numero_conta, pessoas, contas)
        elif opcao == 6:
            listar_contas(contas)
        elif opcao == 0:
            break
        else:
            print("opção inválida")

main()