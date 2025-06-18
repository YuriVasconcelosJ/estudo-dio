class Transporte:
    def mover(self):
        pass


class Carro(Transporte):
    def mover(self):
        print("Dirigindo...")

class Bicicleta(Transporte):
    def mover(self):
        print("Pedalando...")
    
class Aviao(Transporte):
    def mover(self):
        print("Voando...")
    
def usar_transporte(transporte):
    transporte.mover()