class Gerente:
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        self.__senha = senha
        self.__qtd_gerenciados = qtd_gerenciados

    def autentica(self, senha):
        if self.__senha == senha:
            print("acessom permitido")
            return True
        else:
            print("Acesso negado")
            return False
        