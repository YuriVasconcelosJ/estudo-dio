# ITERADORES

# __iter__() e __next__()
# Economizar memória, iterar linha a linha do arquivo

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.indice = 0 # Usar 'indice' é mais claro para essa finalidade

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.indice]
            self.indice += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador(numeros=[20, 40, 60]):
    print(i)