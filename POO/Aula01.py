# Biciletario 

class Bicicleta:
    def __ini__(self, cor, modelo, ano, valor):
        self.cor = cor,
        self.modelo = modelo,
        self.ano = ano,
        self.valor = valor,

    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando bicilceta...")
        print("Bicicleta parada!")
    
    def correr(self):
        print("Vrummmm...")

    def __str__(self):
        return f"Bicicleta: {self.cor}, modelo= {self.modelo}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



