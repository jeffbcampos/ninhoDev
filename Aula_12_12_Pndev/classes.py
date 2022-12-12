class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf


pessoa1 = Pessoa('João', 'M', '123.456.789-00')
print(f"{pessoa1.nome} é do genero {pessoa1.sexo} e seu CPF é {pessoa1.cpf}")