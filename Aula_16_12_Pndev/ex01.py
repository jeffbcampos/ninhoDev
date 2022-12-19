class Conta:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getTitular(self):
        return self.__titular

    def setTitular(self, titular):
        self.__titular = titular

pessoa = Conta('Jeferson', 2500)
print(pessoa.getSaldo())
