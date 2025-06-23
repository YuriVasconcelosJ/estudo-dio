# Criar um sistema bancário com as operações: sacar, depostiar e visualizar extrato

# Conta corrente - armazenar em uma lista, Aconta corrente é composta por = agência, número da conta e user
# numero da conta é sequencial iniciando em 1. O numero da agencia é fixo 0001
# Um user pode ter mais de uma conta, mas uma conta pertence a somente um user
import datetime

LIMITE_SAQUE = 3
NUMERO_AGENCIA = "001"
numero_conta = 1
saldo_conta = 0.0
saques_diarios = 0
extrato = []
lista_usuarios = []
lista_conta_corrente = []
opcoes_menu = ["Depositar", "Sacar", "Extrato", "Criar Usuário", "Criar Conta Corrente", "Listar usuários" ,"Sair"]

# Parte das classes
class PessoaFisica:

    def __init__(self, cpf: str, nome: str, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

        @property
        def cpf(self):
            return self.__cpf
        
        # Verificar futuramente        
        @cpf.setter
        def cpf(self, novo_cpf: str):
            self.__cpf = novo_cpf


        @property
        def data_nascimento(self):
            return self.__data_nascimento

        @data_nascimento.setter
        def data_nascimento(self, nova_data: str):
            try:
               self.__data_nascimento = datetime.datetime.strptime(nova_data, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError
        
        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self, novo_nome: str):
            nome_tratado = novo_nome.strip()
            if len(nome_tratado.split()) >= 2 and nome_tratado.replace(" ", "").isalpha():
                self.__nome = nome_tratado.title()
            else:
                raise ValueError("Nome inválido. Digite o nome completo (pelo menos duas palavras) e sem números.")

class Cliente(PessoaFisica):
    def __init__(self, cpf: str, nome: str, data_nascimento: str, *, logradouro: str, bairro: str, cidade: str, uf: str):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = {"Logradouro": logradouro, "Bairro": bairro, "Cidade": cidade, "UF": uf}
        self.contas = []
    
    def realizar_transacao(conta: Conta, transacao: Transacao):
        ...
    def adicionar_conta(conta: Conta):
        ...

class Conta:
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.historico = historico

    def
        
        

























# Funções de operções
def exibir_menu():
    for indice, opcao in enumerate(opcoes_menu):
        print(f"{indice + 1}. {opcao}")

def buscar_usuario_por_cpf(cpf):
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_usuario(*,nome: str, data_de_nascimento: str, cpf: str, logradouro: str, bairro: str, cidade: str, uf: str):
    # Criar um dicionario
    novo_usuario = {
        "nome": nome,
        "data de nascimento": data_de_nascimento,
        "cpf": cpf, 
        "Endereço": {
            "logradouro": logradouro,
            "bairro": bairro,
            "cidade": cidade,
            "uf": uf
        }
    }
    
    # Verifcar ante de add
    for usuario in lista_usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário com este CPF já criado.")
            return
    lista_usuarios.append(novo_usuario)
    
def depositar_valor(valor: float):
    global saldo_conta
    saldo_conta += valor
    print(f"Valor de R${valor:.2f} depositado com sucesso!")
    extrato.append(f"Depósito: R${valor:.2f}")
    
def verificar_extrato():
    print(5*"= " + "EXTRATO" + 5 * "=")
    if not extrato:
        print("Nenhum extrato registrado nessa conta.")
    for operacao in extrato:
        print(operacao)
    print(f"Saldo atual: R${saldo_conta:.2f}")
    print(10 * "=")

def sacar_valor(valor_saque: float):
    global saldo_conta, saques_diarios

    if valor_saque > saldo_conta:
        print("Saldo insuficente")
    elif valor_saque > 500.00:
        print("Você não pode sacar um valor superior que R$500")
    else:
        saldo_conta -= valor_saque
        extrato.append(f"Saque: R${valor_saque:.2f}")
        print(f"Você sacou R${valor_saque:.2f}")
        saques_diarios += 1

def criar_conta_corrente(user):
    global numero_conta

    conta_corrente = {
        "Agência": NUMERO_AGENCIA,
        "Numero da Conta": numero_conta,
        "Usuário": user
    }
    lista_conta_corrente.append(conta_corrente)
    numero_conta += 1

# FUNÇÕES PARA REALIZAR VERIFICAÇÕES
def input_float_positivo(mensagem: str):
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
            else: 
                print("Valor deve ser maior que 0")
        except ValueError:
            print("Erro: Você não digitou um número válido\n") 

def input_nome():
    while True:
        nome = input("Nome completo: ").strip()
        if len(nome.split()) >= 2 and nome.replace(" ", "").isalpha():
            return nome
        print("Nome inválido. Digite o nome comopleto e sem número")

def input_cpf():
    while True:
        cpf = input("CPF (somente números): ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        print("CPF inválido. Digite exatamente 11 números.")

def input_endereco():
    print("\n--- Endereço ---")
    
    while True:
        logradouro = input("Logradouro (Rua, Avenida etc.): ").strip()
        if logradouro: 
            break
        print("Logradouro não pode estar vazio.")

    while True:
        bairro = input("Bairro: ").strip()
        if bairro: 
            break
        print("Bairro não pode estar vazio.")

    while True:
        cidade = input("Cidade: ").strip()
        if cidade: 
            break
        print("Cidade não pode estar vazia.")

    while True:
        uf = input("UF (ex: PE, SP): ").strip().upper()
        if uf in {"AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT",
                  "MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO",
                  "RR","SC","SP","SE","TO"}:
            break
        print("UF inválida. Digite a sigla de um estado brasileiro.")
    
    return {
        "logradouro": logradouro,
        "bairro": bairro,
        "cidade": cidade,
        "uf": uf
    }

def input_data_nascimento():
    while True:
        data = input("Data de nascimento (DD/MM/AAAA): ").strip()
        
        partes = data.split("/")
        if len(partes) == 3:
            dia, mes, ano = partes
            if dia.isdigit() and mes.isdigit() and ano.isdigit():
                return data
        
        print("Data inválida. Use o formato DD/MM/AAAA.")


while True:
    exibir_menu()
    try:
        opcoes = int(input("Selecione uma opção: "))
    except ValueError:
        print("Erro: você não digitou um número")  
        continue

    # Encerrar aplicação
    if opcoes == 0:
        print("Saindo...")
        break
    
    # Depositar valor 
    if opcoes == 1:
        valor_deposito = input_float_positivo("Digite o valor a ser depositado")
        depositar_valor(valor_deposito)
    
    # Sacar valor 
    elif opcoes == 2:
        if saques_diarios < LIMITE_SAQUE: 
            valor_saque = input_float_positivo("Digite o valor a ser sacado da sua conta")
            sacar_valor(valor_saque)
        else:
            print("Você atingiu a quantidade máxima de saques por hoje.")

    # Verificar extrato
    elif opcoes == 3:
        verificar_extrato()
    
    # Criar usuário
    elif opcoes == 4:
        nome = input_nome()
        data_nascimento =  input_data_nascimento()
        cpf = input_cpf()
        endereco = input_endereco()
        criar_usuario(nome = nome, data_de_nascimento = data_nascimento, cpf = cpf, **endereco)
    
    elif opcoes == 5:
        cpf = input_cpf()
        usuario = buscar_usuario_por_cpf(cpf)
        if usuario:
            criar_conta_corrente(usuario)
        else: 
            print("Usuário não encontrado")
    
    # Futuramente
    elif opcoes == 6:
        ...