from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def calcular_total(self,valor):
        pass


class PagamentoDinheiro(Pagamento):
    def calcular_total(self,valor):
        return valor - (valor * 0.10)

class PagamentoCartaoCredito(Pagamento):
    def calcular_total(self,valor):
        return  valor + (valor * 0.05)


class PagamentoPix(Pagamento):
    def calcular_total(self,valor):
        return   valor - (valor * 0.05)
        
        
def processar_pagamento(pagamento, valor: float):
    print(f"Total a pagar: R$ {pagamento.calcular_total(valor):.2f}")