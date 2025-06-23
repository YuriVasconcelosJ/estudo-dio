from abc import ABC, abstractmethod
from datetime import date

class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transacao(self, transacao: 'Transacao'):
        self._transacoes.append({
            "transacao": transacao,
            "data": date.today().isoformat()
        })
        print(f"Transação de R$ {transacao.valor:.2f} registrada no histórico.")

    def gerar_relatorio(self):
        print("\n--- Histórico de Transações ---")
        if not self._transacoes:
            print("Nenhuma transação registrada.")
            return

        for item in self._transacoes:
            transacao = item["transacao"]
            print(f"Data: {item['data']}, Tipo: {transacao.__class__.__name__}, Valor: R$ {transacao.valor:.2f}")
        print("-----------------------------\n")

class Conta:
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: 'Cliente', historico: Historico):
        self._saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico

    @property
    def saldo(self) -> float:
        return self._saldo

    @staticmethod
    def nova_conta(cliente: 'Cliente', numero: int, agencia: str = "0001") -> 'Conta':
        return Conta(0.0, numero, agencia, cliente, Historico())

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de saque inválido.")
            return False
        if valor > self._saldo:
            print("Saldo insuficiente para saque.")
            return False

        self._saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            print("Valor de depósito inválido.")
            return False

        self._saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self._saldo:.2f}")
        return True
    
    def __str__(self):
        return f"Conta: {self.numero}, Agência: {self.agencia}, Saldo: R$ {self.saldo:.2f}"

class ContaCorrente(Conta):
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.0

    def __init__(self, saldo: float, numero: int, agencia: str, cliente: 'Cliente', historico: Historico, limite: float):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self._saques_hoje = 0

    def sacar(self, valor: float) -> bool:
        if self._saques_hoje >= ContaCorrente.LIMITE_SAQUES:
            print(f"Limite de saques diários ({ContaCorrente.LIMITE_SAQUES}) atingido.")
            return False
        
        if valor > ContaCorrente.LIMITE_VALOR_SAQUE:
            print(f"O valor máximo permitido por saque é de R$ {ContaCorrente.LIMITE_VALOR_SAQUE:.2f}.")
            return False

        if valor > (self.saldo + self.limite):
            print("Saldo e limite insuficientes para saque.")
            return False
        
        if super().sacar(valor):
            self._saques_hoje += 1
            return True
        return False

    def __str__(self):
        return f"Conta Corrente: {self.numero}, Agência: {self.agencia}, Saldo: R$ {self.saldo:.2f}, Limite: R$ {self.limite:.2f}, Saques Restantes Hoje: {ContaCorrente.LIMITE_SAQUES - self._saques_hoje}"

class Cliente:
    def __init__(self, endereco: str, contas: list = None):
        self.endereco = endereco
        self.contas = contas if contas is not None else []

    def realizar_transacao(self, conta: Conta, transacao: 'Transacao') -> bool:
        if conta not in self.contas:
            print(f"Erro: Conta {conta.numero} não associada a este cliente.")
            return False
            
        if transacao.registrar_conta(conta):
            conta.historico.adicionar_transacao(transacao)
            print(f"Transação de R$ {transacao.valor:.2f} realizada com sucesso na conta {conta.numero}.")
            return True
        else:
            print(f"Falha ao realizar transação de R$ {transacao.valor:.2f} na conta {conta.numero}.")
            return False

    def adicionar_conta(self, conta: Conta):
        if conta not in self.contas:
            self.contas.append(conta)
            print(f"Conta {conta.numero} adicionada ao cliente.")
        else:
            print(f"Conta {conta.numero} já está associada a este cliente.")
            
    def __str__(self):
        return f"Cliente: Endereço: {self.endereco}, Contas: {[c.numero for c in self.contas]}"


class PessoaFisica(Cliente):
    def __init__(self, endereco: str, contas: list, cpf: str, nome: str, data_nascimento: date):
        super().__init__(endereco, contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
    def __str__(self):
        return f"Cliente PF: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"


class Transacao(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def registrar_conta(self, conta: Conta) -> bool:
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        super().__init__(valor)

    def registrar_conta(self, conta: Conta) -> bool:
        return conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor: float):
        super().__init__(valor)

    def registrar_conta(self, conta: Conta) -> bool:
        return conta.sacar(self.valor)

# --- Funções do Menu ---

def menu():
    menu_texto = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Cliente
    [q] Sair
    ======================================
    => """
    return input(menu_texto).lower().strip()

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    numero_conta = int(input("Informe o número da conta: "))
    conta = next((c for c in cliente.contas if c.numero == numero_conta), None)

    if not conta:
        print("\n@@@ Conta não encontrada para este cliente! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    deposito = Deposito(valor)
    cliente.realizar_transacao(conta, deposito)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    numero_conta = int(input("Informe o número da conta: "))
    conta = next((c for c in cliente.contas if c.numero == numero_conta), None)

    if not conta:
        print("\n@@@ Conta não encontrada para este cliente! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    saque = Saque(valor)
    cliente.realizar_transacao(conta, saque)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    numero_conta = int(input("Informe o número da conta: "))
    conta = next((c for c in cliente.contas if c.numero == numero_conta), None)

    if not conta:
        print("\n@@@ Conta não encontrada para este cliente! @@@")
        return
    
    print(f"\n--- Extrato da Conta {conta.numero} ---")
    conta.historico.gerar_relatorio()
    print(f"Saldo atual: R$ {conta.saldo:.2f}")
    if isinstance(conta, ContaCorrente):
        print(f"Saques restantes hoje: {ContaCorrente.LIMITE_SAQUES - conta._saques_hoje}")
        print(f"Limite de cheque especial: R$ {conta.limite:.2f}")


def criar_novo_cliente(clientes):
    cpf = input("Informe o CPF do cliente (somente números): ")
    if any(c.cpf == cpf for c in clientes if isinstance(c, PessoaFisica)):
        print("\n@@@ Já existe cliente com este CPF! @@@")
        return

    nome = input("Informe o nome completo do cliente: ")
    data_nascimento_str = input("Informe a data de nascimento (dd-mm-aaaa): ")
    try:
        dia, mes, ano = map(int, data_nascimento_str.split('-'))
        data_nascimento = date(ano, mes, dia)
    except ValueError:
        print("\n@@@ Formato de data inválido. Use dd-mm-aaaa. @@@")
        return

    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/estado): ")

    novo_cliente = PessoaFisica(endereco=endereco, contas=[], cpf=cpf, nome=nome, data_nascimento=data_nascimento)
    clientes.append(novo_cliente)
    print("\n=== Cliente cadastrado com sucesso! ===")

def criar_nova_conta(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if not cliente:
        print("\n@@@ Cliente não encontrado, crie o cliente primeiro! @@@")
        return

    numero_conta = len(contas) + 1  # Lógica simples para número de conta sequencial
    tipo_conta = input("Tipo de conta (cc - Corrente / c - Poupanca - NÃO IMPLEMENTADO): ").lower().strip()

    if tipo_conta == 'cc':
        limite_cheque_especial = float(input("Informe o limite do cheque especial para a Conta Corrente: "))
        nova_conta = ContaCorrente.nova_conta(cliente, numero_conta, "0001", Historico(), limite_cheque_especial)
    elif tipo_conta == 'c':
        print("\n@@@ Contas Poupança ainda não implementadas. Criando Conta Padrão. @@@")
        nova_conta = Conta.nova_conta(cliente, numero_conta, "0001")
    else:
        print("\n@@@ Tipo de conta inválido. Criando Conta Padrão. @@@")
        nova_conta = Conta.nova_conta(cliente, numero_conta, "0001")

    cliente.adicionar_conta(nova_conta)
    contas.append(nova_conta) # Adiciona ao controle global de contas
    print(f"\n=== Conta {nova_conta.numero} criada com sucesso para {cliente.nome}! ===")


def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada! @@@")
        return
    for conta in contas:
        print("=" * 100)
        print(str(conta))
        print(f"Cliente: {conta.cliente.nome}, CPF: {conta.cliente.cpf}") # Acessando dados do cliente
    print("=" * 100)


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nc":
            criar_nova_conta(clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "nu":
            criar_novo_cliente(clientes)
        elif opcao == "q":
            print("\nSaindo do sistema. Obrigado por usar!")
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

if __name__ == "__main__":
    main()