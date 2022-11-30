def calc():
    n1 = input("Digite o primeiro numero: ")
    n2 = input("Digite o segundo numero: ")
    op = input("Digite o operador (+, -, *, /): ")
    res = eval(n1+op+n2)
    return res

print(calc())


