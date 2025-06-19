# Variáveis de classe e Variáveis de Instância
# Variáceis de Classe - As variáveis de classe são declaradas dentro da definição da classe, mas fora de qualquer método. - São compartilhadas por todos os objetos(classe)
# Variáveis da instância - As variáveis de instância são declaradas dentro de um método da classe, geralmente no método __init__, e são prefixadas com self.. Elas são exclusivas para cada instância da classe. Cada objeto tem sua própria cópia dessas variáveis.
class Pessoa:
    especie = "Humano" # Variável da classe

    def __init__(self, nome):
        self.nome # Variável da instância
    
p1 = Pessoa("Yuri")
p2 = Pessoa("Ana")

print(p1.especie)
print(p2.especie)

Pessoa.especie = "Home Sapiens"

print(p1.especie)
print(p2.especie)

print(Pessoa.__)