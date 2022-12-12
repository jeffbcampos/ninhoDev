

# Equipe Perdidos

# palavra = input("Digite uma palavra: ")
# letra = input("Escolha uma letra pra ser contada: ")

# print(f"Na palavra {palavra} tem {palavra.count(letra)} letras {letra}")

#Equipe2Cateq



# def check(senha):
#     if senha.isnumeric() == True:
#         if len(senha) < 4 or len(senha) > 8:
#             print("A senha nao tem o tamanho determinado")

#         else:
#             print("Senha cadastrada com sucesso!")
#             global repetir
#             repetir = False
            
#     else:
#         print("A senha não pode ter outros chars que não seja numeros! Cadastro Cancelado")

# repetir = True

# while(repetir):
#     senha = input('Digite uma senha de minimo 4 digitos e maximmo 8 digitos: ')
#     check(senha)

# Equipe 5 Alpha Pythonista
# def calc():
    
#     n1 = input("Digite o primeiro numero: ")
#     op = input("Digite o operador (+, -, *, /, **, %(raiz)): ")
#     if op == '%':
#         res = float(n1) ** 0.5
#         print(res)
#     else:
#         n2 = input("Digite o segundo numero: ")    
#         res = eval(n1+op+n2)
#         print(res)
#     while True:
#         op = input("Digite o operador (+, -, *, /, **, ): ")
#         n3 = input("Digite um numero: ")
#         res = eval(str(res)+ op +n3)
#         print(res)
# print(calc())

#Desafio da equipe nossa
# global repetir

# repetir = True
# while(repetir):
#     repetir = False
#     num =input("Digite um numero inteiro de ate 4 digitos: ")
#     if num.isnumeric() == False:
#         print("Não e um numero inteiro, Favor digite novamente")
#         repetir = True
#     else:

#         num = int(num)
#         u = num // 1 % 10
#         d = num // 10 % 10
#         c = num // 100 % 10
#         m = num // 1000 % 10
#         print(f"O número tem {u} unidades")
#         print(f"O número tem {d} dezenas")
#         print(f"O número tem {c} centenas")
#         print(f"O número tem {m} unidades de milhar")
unidades = ('unidades', 'dezenas', 'centenas', 'unidade de milhar')


numero = input("Escreva um numero de 4 digitos: ")
#numero = numero[::-1]
for i in range(len(numero)):
    print(f"{unidades[-i-1]} = {numero[i]}")
