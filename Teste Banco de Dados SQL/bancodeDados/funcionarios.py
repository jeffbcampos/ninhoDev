import json

class Funcionario:
    def __init__(self, ud, nome, salario):        
        self._nome = nome
        self._salario = salario
        self._ud = ud


def adicionarFuncionario(funcionarios):
    novoFuncionario = input("Digite o nome do novo funcionário: ")
    novoFuncionarioSalario = float(input(f"Digite o salario de {novoFuncionario}: "))
    funcionarios.append(Funcionario(len(funcionarios) + 1, novoFuncionario, novoFuncionarioSalario))
    print(f"{novoFuncionario} foi adicionado com sucesso")


def salvarBancodeDados(listadeFuncionarios):
    novoBanco = []

    for i in funcionarios:
        novoBanco.append({"ID": i._ud, "Nome": i._nome, "Salario": i._salario})

    with open(r'C:\Users\ADMIN\Desktop\Lógica\Teste Banco de Dados SQL\bancodeDados\banco.json', 'w') as nb:
        json.dump(novoBanco, nb, indent=2)
    
    print("Banco Salvo com Sucesso!")



with open("C:/Users/ADMIN/Desktop/Lógica/Teste Banco de Dados SQL/bancodeDados/banco.json") as b:
    banco = json.load(b)

funcionarios = []

for funcionario in banco:
    funcionarios.append(Funcionario(funcionario["ID"], funcionario["Nome"], funcionario["Salario"]))

for i in range(len(funcionarios)):
    print(f"{i + 1} - {funcionarios[i]._nome}")

while True:
    opcao = input('''
    1- Ver Funcionários
    2- Ver salário Funcionário
    3- Adicionar Funcionário
    0 - Sair da Aplicação
    ''')

    match opcao:
        case "1":
            for i in range(len(funcionarios)):
                print(f"{i + 1} - {funcionarios[i]._nome}")
        case "2":
            ud = int(input("Digite o ID do funcionário que você deseja ver o salário: "))
            print(f"O salário de {funcionarios[ud -1]._nome} é {funcionarios[ud -1]._salario}")
        case "3":
            adicionarFuncionario(funcionarios)
        case "0":
            print("Finalizando programa e salvando Dados...")
            salvarBancodeDados(funcionarios)
            break






        