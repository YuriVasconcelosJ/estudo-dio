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
print(numeros[::-1]) # matriz inversa
