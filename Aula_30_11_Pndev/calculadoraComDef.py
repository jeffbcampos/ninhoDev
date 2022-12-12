
def calculadora(n1, n2, op):

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
        if(num2 == 0):
            global validador
            validador = True
            return "O segundo número não pode ser zero"
        res = num1 / num2
        return res
    if (op == '+' or op == 'SOMA'):
        print(f"{soma(n1, n2):.2f}")            
    elif (op == '-' or op == 'SUBTRACAO'):
        print(f"{sub(n1, n2):.2f}")            
    elif (op == '*' or op == 'MULTIPLICACAO'):
        print(f"{multi(n1, n2):.2f}")            
    elif (op == '/' or op == 'DIVISAO'):
        print(f"{divi(n1, n2)}")            
    else:
        print("Operador inválido!")
validador = True

while(validador):

    validador = False
            
    n1 = input("Digite o primeiro número: ")
    if n1.isnumeric() or n1.replace('.', '', 1).isnumeric():
        n1 = float(n1)
        n2 = input("Digite o segundo número: ")
        if n2.isnumeric() or n2.replace('.', '', 1).isnumeric():
            n2 = float(n2)
            op = input("Digite a operação (+(SOMA), -(SUBTRACAO), /(DIVISAO), *(MULTIPLICACAO)): ").upper()
            calculadora(n1, n2, op) 
        else:
            print("O número 2 é inválido!")
            validador = True
    else:
        print("Número 1 é inválido!")
        validador = True
