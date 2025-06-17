# LISTA
# Coleção ordenada e mutável, podemos armazenar qualquer tipo de dados
# Permite elementos duplicados e seu índice inicial é 0
# Mutável(Podo alterar, adicionar e remover itens)

# Exemplos:
lista_vazia = []
frutas = ["maça", "banana", "uva", "abacaxi"]
print(frutas)
numeros = list(range(10))
letras = list("Python")
carro = ["Ferrari", "F8", 420000, 2020, 2900, "SP", True]

# Como acessar elemento em uma lista:
print(frutas[0]) # Maça
print(frutas[-1]) # Abacaxi OBS.: O índice negativo indica que vai percorrer de trás para frente

# Listas aninhadas

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0]) # [1, 2, 3]
print(matriz[0],[1]) # 2 -> linha 0, coluna 1
print(matriz[2],[2]) # 9 -> Linha 2, Coluna 2 

# Fatiamento
# lista[inicio: fim: passo]
numeros = [10, 20, 30, 40, 50, 60, 70]
print(numeros[1:4]) # [20, 30, 40]
print(numeros[:3]) # [10, 20, 30]
print(numeros[::]) # [70, 60, 50, 40, 30, 20, 10] 
print(numeros[::-1]) # matriz inversa

# Iterar Listas
# Percorremos utilizando um laço for

carros = ["Gol", "Celta", "Palio"]

for carro in carros:
    print(carro)

# Função enumerate - Coloca indices nos enumerados

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}") 

# Comprenssão de listas

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Outra maneira de fazer o filtro
pares =  [numero for numero in numeros if numero % 2 == 0]

# Exemplo dois

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrados = []

for numero in numeros: 
    quadrados.append(numero ** 2)

numeros_quadrados = [numero ** 2 for numero in numeros]