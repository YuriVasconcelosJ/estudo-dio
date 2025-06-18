# Getter e setter

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome 
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) < 2:
            raise ValueError("O nome deve ter pelo menos 2 letras.")
        self.__nome = novo_nome
    

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def set_idade(self, nova_idade):
        if not isinstance(int, nova_idade):
            raise ValueError("Idade não é inteira")
        self.__idade = nova_idade

