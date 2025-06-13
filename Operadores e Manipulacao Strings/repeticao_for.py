# FOR

texto = input("Informe um texto: ")
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

# Função range

# função built-in do python range(stop, start e step)

for numero in range (0, 10, 2):
    print(numero, end="")
    # 0, 2, 4, 6, 8, 10

# While é usado para quando não sabemos quantas vezes o nosso bloco tem q executar

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \2[2] Extrato \n[0] Sair \n:"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato")

# BREAK e CONRINUE