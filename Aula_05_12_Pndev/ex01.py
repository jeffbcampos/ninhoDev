# n1 = 2.3
# print(type(n1) == int)

global repetir

def exercicio():
    repetir = True
    while(repetir):
        num = input("Digite um número inteiro: ")
        if(num.isnumeric()):
            repetir = False
            print("Fim")
        else:
            print("Não ´inteiro")

exercicio()