class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def porcentualAumento(self, porcentagem):
        self.salario = self.salario + (self.salario * (porcentagem / 100))


funcionario1 = input('Digite o nome do funcionário: ')

salario = float(input('Digite o salário do funcionário: '))

funcionario = Funcionario(funcionario1, salario)

porcentagem = float(input('Digite a porcentagem de aumento: '))
funcionario.porcentualAumento(porcentagem)

print(f'O novo salário do funcionário {funcionario.nome} é {funcionario.salario}')