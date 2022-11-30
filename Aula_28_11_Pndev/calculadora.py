def soma(num1, num2):
    res = num1 + num2
    return res
def sub(num1, num2):
    res = num1 - num2
    return res
def multi(num1, num2):
    res = num1 * num2
    return res
def divi(num1, num2):
    res = num1 / num2
    return res


repetir = True

num1 = ''
num2 = ''

while(repetir):
    
    while(num1.isnumeric() != True or num2.isnumeric() != True):
        num1 = input("Digite o primeio número: ")
        if(num1.isnumeric() == False):        
            print("Não é numero")
        num2 = input("Digite o segundo número: ")
        if(num2.isnumeric() == False):        
            print("Não é numero")     
    num1 = float(num1)
    num2 = float(num2)
    operador = input("Digite a operação (+, -, /, *): ").upper()

    if(operador == "+" or "SOMAR"):
        print(soma(num1, num2))
        repetir = False
    elif(operador == "-" or "SUBTRAÇÂO"):
        print(sub(num1, num2))
        repetir = False
    elif(operador == "*" or "MULTIPLICACAO"):
        print(multi(num1, num2))
        repetir = False
    elif(operador == "/" or "DIVISAO"):
        print(divi(num1, num2))
        repetir = False
    else:
        print("Operador inválido")
