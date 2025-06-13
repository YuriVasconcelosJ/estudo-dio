curso = "pYthon"

print(curso.upper()) # PYTHON

print(curso.lower()) # python

print(curso.title()) # Python

curso = "      Pyhton          "

print(curso.strip()) # Python

print(curso.lstrip()) # "Python    "

print(curso.rstrip()) # "   Python"

curso = "Python"

print(curso.center(10, "#")) # "##Python##"

print(".".join(curso)) # P.y.t.h.o.n

# INTERPOLAÇAO DE VARIÁVEIS
nome = "Yuri"
idade = 28
profissao = 'Programador'
lingugagem = "Python"

# Antigo estilo
print("Olá, me chamo %s. Eu tenoh %d anos de idade, tabalho com %s e estou matriculado no curso de %s." % (nome, idade, profissao, lingugagem))

# Método format
print("Olá, me chamo {}. Eu tenoh {} anos de idade, tabalho com {} e estou matriculado no curso de {}."  .format(nome, idade, profissao, lingugagem))

# Método f-string
print("Olá, me chamo {nome}. Eu tenoh {idade} anos de idade, tabalho com {profissao} e estou matriculado no curso de {curso}")

#  Formatar strings com f-string
PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # Valor de PI: 3.14

print(f"Valor de PI: {PI:10.2f}") # "Valor de PI:     3.14"


# Fatiamento de strings

# retorna um substring partes da string original
# [start: stop, [step]]

nome = "Yuri Jesus Vasconcelos"

nome[0] # Y

nome[:4] # Yuri

nome[5:] # Jesus Vasconcelos

nome[5::2] # Vai pular em dois em dois

nome[::-1] # inverte tudo