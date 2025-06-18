# Simulando uma loja
class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco
    
    @property
    def estoque(self):
        return self.__estoque
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @preco.setter
    def preco(self, preco_novo):
        self.__preco = preco_novo

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser maior que 0")
        self.__estoque += quantidade
    
    def remover_estoque(self, quantidade):
        if self.__estoque <= 0:
            raise ValueError("Quantidade deve ser positiva")
        if quantidade > self.__estoque:
            raise ValueError("Estoque insuficiente")
        self.__estoque -= quantidade


    def vender_estoque(self, quantidade): 
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        if quantidade > self.__estoque:
            print(f"Não há quantidade suficiente para vender: {quantidade} unidades")
        else:
            print("Venda realizada com sucesso!")
            self.__estoque -= quantidade