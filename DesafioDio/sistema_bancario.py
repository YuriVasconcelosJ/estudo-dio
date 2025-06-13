# Criar um sistema bancário com as operações: sacar, depostiar e visualizar extrato

saldo_conta = 0.0
saques_diarios = 0
extrato = []
LIMITE_SAQUE = 3


def input_float_positivo(mensagem):
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


while True:
    opcoes = input("Selecione uma das seguintes opções: [1]Sacar, [2]Depositar, [3]Extrato, [0]Sair")
    try:
        opcoes = int(opcoes)
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
       saldo_conta += valor_deposito
       print(f"Valor de R${valor_deposito:.2f} depositado com sucesso!")
       extrato.append(f"Depósito: R${valor_deposito:.2f}")
    
    # Sacar valor
    elif opcoes == 2:
        if saques_diarios < LIMITE_SAQUE: 
            valor_saque = input_float_positivo("Digite o valor a ser sacado da sua conta")
            if valor_saque > saldo_conta:
                print("Saldo insuficente")
                continue
            elif valor_saque > 500.00:
                print("Você não pode sacar um valor superior que R$500")
                continue
            saldo_conta -= valor_saque
            extrato.append(f"Saque: R${valor_saque:.2f}")
            print(f"Você sacou R${valor_saque:.2f}")
            saques_diarios += 1
        else:
            print("Você atingiu a quantidade máxima de saques por hoje.")


    # Verificar extrato
    elif opcoes == 3:
        print(5*"= " + "EXTRATO" + 5 * "=")
        if not extrato:
            print("Nenhum extrato registrado nessa conta.")
        for operacao in extrato:
            print(operacao)
        print(f"Saldo atual: R${saldo_conta:.2f}")
        print(10 * "=")

    else:
        print("Opção inválida. Tente novamente.")
