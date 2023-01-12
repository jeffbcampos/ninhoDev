import json
from classFuncionario import Funcionario, Gerente
from classEmpresa import Empresa
import getpass

with open(r"C:\Users\NatyeJeff\Documents\Codigos Python\Codigos_Python\exercicioBancoNinho\banco.json") as f:
    dados = json.load(f)

def salvarBanco(funcionarios):
    novoBanco = []
    for func in funcionarios:
        if func._cargo == "Gerente":
            novoBanco.append({"ID": func._id, "Nome": func._nome, "Cpf": func._cpf, "Salario": func._salario, "Cargo": func._cargo, "Login": func.login, "Senha": func.senha})
        else:
            novoBanco.append({"ID": func._id, "Nome": func._nome, "Cpf": func._cpf, "Salario": func._salario, "Cargo": func._cargo})

    with open(r"C:\Users\NatyeJeff\Documents\Codigos Python\Codigos_Python\exercicioBancoNinho\banco.json", "w") as f:
        json.dump(novoBanco, f, indent=2)    


funcionarios = []

for func in dados:
    if func["Cargo"] == "Gerente":
        funcionarios.append(Gerente(func["ID"], func["Nome"], func["Cpf"], func["Salario"], func["Cargo"], func["Login"], func["Senha"]))
    else:
        funcionarios.append(Funcionario(func["ID"], func["Nome"], func["Cpf"], func["Salario"], func["Cargo"]))

empresa = Empresa(funcionarios)


def find_index(lista, chave, valor):
    for i, dic in enumerate(lista):        
        if dic[chave] == valor:
            return i + 1
    return -1

def login():
    id = input("Digite seu ID: ")
    autenticado = False
    while autenticado == False:        
        for func in dados:       
            if func["ID"] == int(id):
                if func["Cargo"] == "Gerente":
                    login = input("Digite seu login: ")
                    if func["Login"] == login:           
                        gerenteLogin = Gerente(func["ID"], func["Nome"], func["Cpf"], func["Salario"], func["Cargo"], func["Login"], func["Senha"])
                        senha = getpass.getpass("Digite a senha: ")
                        autenticado = gerenteLogin.autenticar(login, senha)
                        if autenticado == True:                        
                            return menuGerente(gerenteLogin)
                        elif autenticado == False:
                            print("Login inválido")
                                                
                        # menuGerente(gerenteLogin)
                        # if gerenteLogin.senha == senha:
                        #     print("Acesso permitido")                        
                        # else:
                        #     print("Acesso negado")
                        #     return None                       
                    else:
                        print("Login inválido")
                        
                else:        
                    funcionarioLogin = Funcionario(func["ID"], func["Nome"], func["Cpf"], func["Salario"], func["Cargo"])
                    print("Logado como funcionário")
                    return menuFuncionario(funcionarioLogin)        
        
    print("ID não encontrado")


# def removerFuncionario(funcionarios, id):        
#         id = int(input("Digite o ID: "))
#         funcionarios.pop(id-1)

def menuGerente(gerente):
    while True:
        print(f"\nBem vindo, {gerente.get_nome()}")
        print("1 - Cadastrar funcionário")
        print("2 - Alterar funcionário")
        print("3 - Remover funcionário")
        print("4 - Listar funcionários")
        print("5 - Sair e Salvar no Banco de Dados")
        opcao = input("\nDigite a opção desejada: ")        
        if opcao == '1':
            gerente.cadastrarFuncionario(funcionarios)
            salvarBanco(funcionarios)
        elif opcao == '2':
            gerente.alterarFuncionario(funcionarios)
        elif opcao == '3':
            id = input("Digite o ID: ")
            idRemove = find_index(dados, "ID", id)
            print("Removendo Funcionário...")
            funcionarios.pop(idRemove)            
        elif opcao == '4':
            gerente.listarFuncionarios(funcionarios)
        elif opcao == '5':
            print("Saindo e Salvando no Banco de Dados...")
            salvarBanco(funcionarios)
            print("Salvo no Banco com sucesso!")            
            break        
        else:
            print("\nOpção inválida")
            
def menuFuncionario(funcionario):
    while True:
        print(f"\nBem vindo, {funcionario.get_nome()}")
        print("1 - Alterar dados")
        print("2 - Listar dados")
        print("3 - Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == '1':
            funcionario.alterarDados(funcionario)
        elif opcao == '2':
            funcionario.listarDados()
        elif opcao == '3':
            print("Saindo...")
            salvarBanco(funcionarios)
            break        
        else:
            print("Opção inválida") 


login()