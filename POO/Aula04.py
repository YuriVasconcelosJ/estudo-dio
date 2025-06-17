# Encapsulamento em Python

# Python - Não tem modificadores de acesso com, utilizamos convenção

# nome - Acessível de fora
# _nome - Protegido
# __nome - Atributo privado(name mangling)

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def mostrar_saldo(self):
        return self.__saldo