# Classes abstratas - devemos importar ABC, abstractmethod
# Devemos utilizar o decorador @abstactmethod
# Não podemos instanciar uma classe 
from abc import ABC, abstractmethod

class Animal(ABC):

    # emitir_som é um método abstrato, ou seja, as subclasses são obrigadas a implementá-lo.
    @abstractmethod
    def emitir_som(self):
        pass

# a = Animal()  # Erro! TypeError: Can't instantiate abstract class

class Cachorro(Animal):

    def emitir_som(self):
        return "Au Au"
    
c = Cachorro()
print(c.emitir_som())

class Forma(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado * self.lado
    
q = Quadrado(5)
print(q.calcular_area()) # 25