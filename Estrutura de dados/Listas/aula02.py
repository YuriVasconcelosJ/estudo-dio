lista = []

# Adicionando valores ao final de cada lista
lista.append(1)
lista.append("Python")
lista.append([30, 40,50])

# Limpando uma lista
lista.clear()
print(lista) # []

# Copiando uma lista
lista1 = [1, 2, 3]
lista2 = lista1

lista2.append(4)
print(lista1) # [1, 2, 3, 4]

lista1 = [1, 2, 3]
lista2 = lista1.copy() # Dessa forma, eles vão apontar para outro objeto na memória

# Copy não realiza cópia profunda
lista1 = [[1, 2], [3, 4]]
lista2 = lista1.copy()

lista2[0][0] = 99
print(lista1)  # [[99, 2], [3, 4]]  

# # Maneira de copiar
# import copy
# lista2 = copy.deepcopy(lista1)

# Adicionando mais de um elemento na lista
linguagens = ["Python", "JS", "C"]

print(linguagens)

linguagens.extend(["Java", "Csharp"])

print(linguagens) # ["Python", "JS", "C", "Java", "Csharp"]

# Retornar o index da lista

linguagens = ["Python", "JS", "C", "Java", "Csharp"]
linguagens.index("Java") # 3
linguagens.index("Python") # 0
linguagens.index("Lua") # ValueError: Lua is not in list

# Excluir elementos da lista por meio de seu índice

linguagens = ["Python", "JS", "C", "Java", "Csharp"]
linguagens.pop() # Csharp
linguagens.pop() # Java
linguagens.pop() # C
linguagens.poo(0) # Python

# Excluir elemento da lista por meio de seu nome
linguagens = ["Python", "JS", "C", "Java", "Csharp"]
linguagens.remove("C")
print(linguagens) # ["Python", "JS", "Java", "Csharp"]

# Inverter uma lista

linguagens = ["Python", "JS", "C", "Java", "Csharp"]

linguagens.reverse()
print(linguagens) # ["Csharp", "Java", "C", "JS", "Python"]

# Verificar tamanho da lista
linguagens = ["Python", "JS", "C", "Java", "Csharp"]
len(linguagens) # 5

#  Ordenar lista
linguagens = ["Python", "JS", "C", "Java", "Csharp"]
linguagens.sort() # Odena em ordem alfabética

linguagens = ["Python", "JS", "C", "Java", "Csharp"]
linguagens.sort(reverse=True) # Ordem alfabética invertida

linguagens.sort(key= lambda x : len(x) ) # Ordna pala quantidade de letras

linguagens.sort(key= lambda x : len(x), reverse=True) # Ordna pala quantidade de letras invertida

linguagens.insert(0,)