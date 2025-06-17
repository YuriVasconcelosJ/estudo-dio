# Classe em python 
class Pessoa:
    qtd_pessoas_criadas = 0
    especie = "Humano" # Variável da classe - Compartilhada por todos da instância da classe

    def __init__(self, nome, idade): # Método de inicialização da classse
        self.nome = nome
        self.idade = idade
        self.__class__.qtd_pessoas_criadas += 1
   
    def apresentar(self): # Métodos da instância 
        print(f"Olá, meu nome é {self.nome} e sou um {self.__class__.especie}")

    # Com esse classmethod não precisamos instancia um objeto para acessar e verificar a quantidae de pessoas
    @classmethod
    def obter_qtd_pessoas(cls): # Perceba que devemos utilizar o Pessoa ao invés do self
        print(f"{cls.qtd_pessoas_criadas} pessoas foram criadas")
