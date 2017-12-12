from Cliente import Cliente

class Conta:
    def __init__(self, numero, saldo, titular, limite):
        self.__numero = numero
        self.__saldo = saldo
        self.__titular = Cliente(titular)
        self.__limite = limite

    def saca(self,valor):
        if(self.__saldo >= valor and valor > 0):
            self.__saldo -= valor
            return True
        else:
            print("Saldo Insuficiente!")
            return False        

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        valor_a_autorizar = self.saca(valor)
        if (valor_a_autorizar == True):
            destino.deposita(valor)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property           
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.nome

    @staticmethod
    def codigo_banco():
        return "001"