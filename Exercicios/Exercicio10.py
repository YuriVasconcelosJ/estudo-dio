# Exercício – Controle de Espécie

class Animal:
    especie_padrao = "Desconhecida"
    
    def __init__(self, nome_da_especie):
        self.nome_da_especie = nome_da_especie
    
    def mostrar_especie(self):
        return f"{self.nome} é da espécie: {self.especie_padrao}"

a1 = Animal("Cachorro")
a2 = Animal("Gato")

Animal.especie_padrao = "Mamífero"
a1.especie_padrao = ("Canino")

print(a1.mostrar_especie())  
print(a2.mostrar_especie())        