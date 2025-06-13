import sys


saldo = 2000.0
saque = float(input("Informe o valor do saque"))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")

# Utilizando if/else
saldo = 2000.0
saque = float(input("Informe o valor do saque"))

if saldo >= saque:
    print("Realizando saque!")
else: 
    print("Saldo insuficiente!")

# Utilizanod if/elif/else

opcao = int(input("Infomre uma opção: [1] Sacar \n [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque:"))
    ...
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12
idade = int(input("Informe sua idade:"))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade <= IDADE_ESPECIAL:
    print("Pode iniciar as aulas teóricas")
else:
    print("Ainda não pode tirar a cnh")

# if aninhado


# if ternario 
# Deve ser armazenado em uma variavel 
total = "Saque realizado" if saldo >= 500.00 else "Saldo inválido" 