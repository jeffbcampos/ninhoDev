class Funcionario:
    def __init__(self, id, nome, cpf, salario, cargo):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._cargo = cargo

    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id
    
    def get_nome(self):
        return self._nome
    def set_nome(self, nome):
        self._nome = nome

    def get_cpf(self):
        return self._cpf
    def set_cpf(self, cpf):
        self._cpf = cpf

    def get_salario(self):
        return self._salario
    def set_salario(self, salario):
        self._salario = salario

    def get_cargo(self):
        return self._cargo
    def set_cargo(self, cargo):
        self._cargo = cargo

    def alterarDados(self,funcionario):
        print("Alterando dados")
        funcionario.set_nome(input("Digite o nome: "))
        funcionario.set_cpf(input("Digite o CPF: "))

    def listarDados(self):
        print("\nListando dados\n")
        print(f"ID: {self.get_id()}")
        print(f"Nome: {self.get_nome()}")
        print(f"CPF: {self.get_cpf()}")
        print(f"Salário: {self.get_salario()}")
        print(f"Cargo: {self.get_cargo()}\n")

               

        

class Gerente(Funcionario):
    def __init__(self, id, nome, cpf, salario, cargo, login, senha):
        super().__init__(id, nome, cpf, salario, cargo)
        self.login = login
        self.senha = senha

    def autenticar(self, login, senha):
        if self.login == login and self.senha == senha:
            print('Acesso permitido')
        else:
            print('Acesso negado')

    def cadastrarFuncionario(self, funcionarios):
        print("Cadastrando funcionário")
        # id = int(input("Digite o ID: "))
        nome = input("Digite o nome: ")
        cpf = input("Digite o CPF: ")
        salario = float(input("Digite o salário: "))
        cargo = input("Digite o cargo: ")
        if cargo == "Gerente":
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            funcionarios.append(Gerente(len(funcionarios) + 1, nome, cpf, salario, cargo, login, senha))
        else:
            funcionarios.append(Funcionario(len(funcionarios) + 1, nome, cpf, salario, cargo))

    def alterarFuncionario(self, funcionarios):
        print("Alterando funcionário\n")
        id = int(input("Digite o ID: "))
        print("Funcionário Escolhido: \n")
        print(f"ID: {funcionarios[id-1].get_id()}")
        print(f"Nome: {funcionarios[id-1].get_nome()}")
        print(f"CPF: {funcionarios[id-1].get_cpf()}")
        print(f"Salário: {funcionarios[id-1].get_salario()}")
        print(f"Cargo: {funcionarios[id-1].get_cargo()}\n")                
        salario = float(input("Digite o salário: "))
        cargo = input("Digite o cargo: ")
        if cargo == "Gerente":
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            funcionarios[id-1] = Gerente(id, funcionarios[id-1].get_nome(), funcionarios[id-1].get_cpf(), funcionarios[id-1].set_salario(salario), funcionarios[id-1].set_cargo(cargo), login, senha)
        else:
            funcionarios[id-1].set_salario(salario)
            funcionarios[id-1].set_cargo(cargo)       
        

    def removerFuncionario(self, funcionarios):
        print("Removendo funcionário")
        id = int(input("Digite o ID: "))
        funcionarios.pop(id-1)

    def listarFuncionarios(self, funcionarios):
        print("Listando funcionários\n")
        for func in funcionarios:
            print(f"ID: {func.get_id()}")
            print(f"Nome: {func.get_nome()}")
            print(f"CPF: {func.get_cpf()}")
            print(f"Salário: {func.get_salario()}")
            print(f"Cargo: {func.get_cargo()}\n")

