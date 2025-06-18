from abc import ABC, abstractmethod

class Produto:
    def __init__(self, nome: str, preco: float, qtd_estoque: int):
        self.nome = nome          
        self.preco = preco       
        self.qtd_estoque = qtd_estoque  
    # --- Nome ---
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("Nome deve ser uma string não vazia.")
        self.__nome = novo_nome.strip()

    # --- Preço ---
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if not isinstance(novo_preco, (int, float)) or novo_preco < 0:
            raise ValueError("Preço deve ser um número positivo.")
        self.__preco = float(novo_preco)

    # --- Estoque ---
    @property
    def qtd_estoque(self):
        return self.__qtd_estoque

    @qtd_estoque.setter
    def qtd_estoque(self, nova_qtd: int):
        if not isinstance(nova_qtd, int) or nova_qtd < 0:
            raise ValueError("Quantidade em estoque deve ser um inteiro não negativo.")
        self.__qtd_estoque = nova_qtd

    # --- Métodos ---
    def baixar_estoque(self, qtd: int):
        if not isinstance(qtd, int) or qtd <= 0:
            raise ValueError("A quantidade a baixar deve ser um número inteiro positivo.")
        if qtd > self.__qtd_estoque:
            raise ValueError("Estoque insuficiente.")
        self.__qtd_estoque -= qtd

class ItemPedido:
    def __init__(self, produto, quantidade: int):
        if not isinstance(quantidade, int) or quantidade <= 0:
            raise ValueError("A quantidade deve ser um número inteiro positivo")
        self.produto = produto
        self.quantidade = quantidade
    
    def subtotal(self):
        return self.produto.preco * self.quantidade
    
    def confirmar_item(self):
        self.produto.baixar_estoque(self.quantidade)

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    # -- Nome --
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise ValueError("Nome deve ser uma string não vazia")
        self.__nome = novo_nome.strip()
    
    # --cpf
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if not isinstance(novo_cpf, str) or not novo_cpf.isdigit() or len(novo_cpf) != 11:
            raise ValueError ("CPF deve conter exatamente 11 dígitos numéricos.")
        self.__cpf = novo_cpf    

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.lista_item_pedido = []
    
    def adicionar_item(self, produto, qtd: int):
        item = ItemPedido(produto, qtd)
        self.lista_item_pedido.append(item)
    
    def calcular_total(self):
        return sum(item.subtotal() for item in self.lista_item_pedido)
    
    def confirmar_pedido(self):
        for item in self.lista_item_pedido:
            item.confirmar_item()
    
class Pagamento(ABC):
    @abstractmethod
    def calcular_pagamento(self,valor):
        pass


class PagamentoDinheiro(Pagamento):
    def calcular_pagamento(self,valor):
        return valor - (valor * 0.10)

class PagamentoCartaoCredito(Pagamento):
    def calcular_pagamento(self,valor):
        return valor + (valor * 0.05)

class PagamentoPix(Pagamento):
    def calcular_pagamento(self,valor):
        return valor - (valor * 0.05)