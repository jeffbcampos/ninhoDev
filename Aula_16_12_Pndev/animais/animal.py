class Animal:
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor

    def comer(self):
        print(f"o animal {self.__nome} está comendo")