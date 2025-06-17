# Sets - Coleção que não possui objetos repetidos usamos sets para representar conjuntos matemáticos e eliminar itens duplicados de iterável

set([1, 2, 3, 4, 5, 6])

set("abacaxi")

# Aceessando os dados em um set: Devemos converter em uma lista

numeros = {1, 2, 3, 4}
numeros = list(numeros)

numeros[0]

# Percorrendo carro

carros = {"gol", "palio", "sandero"}

for indice, carro in enumerate(carros):
    print(indice, carro)


# unio
conjunto_a = {1, 3}
conjunto_b = {2, 4}

conjunto_a.union(conjunto_b)

# intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b)

# difference

conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4} 

# symmetric_difference

conjunto_a.symmetric_difference(conjunto_b) # {1, 4}

# issubset

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False

# issuperset

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True

# isdisjoint

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # True
conjunto_a.isdisjoint(conjunto_c) # False

# add

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}

# copy - mesma coisa do list

# discard - Vc escolhe o valor para tirar, mas não retorna um valor

# pop - tira o valor da frente

# remove - vc escolhe o valor para tirar do set, mas retornar um erro  