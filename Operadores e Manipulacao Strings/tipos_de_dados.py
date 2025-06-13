# Tipos em Python

# Texto = str
# Numérico = int, float, complex
# Sequência = list, tuple, range
# Mapa = dict
# Coleção = set, fronzenset
# Booleano = bool
# Binário = bytes, bytearray, memoryview

# TEXTO

texto = 'olá mundo'
print(type(texto)) # <class 'str'>

# NUMERICO

x = 15
print(type(x)) # <class 'int'>

y = 3.14
print(type(y)) # <class 'float'>

z = 2 + 3j
print(type(z)) # <class 'complex'>

# SEQUENCIA

lista = [1, 2, 3]
print(type(lista)) # <class 'list'>

tupla = (1, 2, 3)
print(type(tupla))

intervalo = range(5)
print(type(intervalo))

# Mapa

# dict
pessoa = {"nome": "Yuri", "idade": 21}
print(type(pessoa)) # <class 'dict'>

# COLECAO

# set
conjunto = {1, 2 ,3}
print(type(conjunto)) # <class 'set'>

# fronzenset
conjunto_fixo = frozenset([1, 2, 3])
print(type(conjunto_fixo))  # <class 'frozenset'>

# BOOLEAN

verdade = True
falso = False
print(type(verdade))  # <class 'bool'>

# BINARIO

dados = b"abc"
print(type(dados))  # <class 'bytes'>

dir(100)