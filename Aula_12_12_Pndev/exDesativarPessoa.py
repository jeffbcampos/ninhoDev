class Pessoa:
    def __init__(self, nome, idade, cpf, ativo):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.ativo = ativo
    
    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso!")

pessoa1 = Pessoa('João', 20, '123.456.789-00', True)

pessoa1.desativar()

if pessoa1.ativo:
    print('A pessoa está ativa')
else:
    print('A pessoa está desativada')

