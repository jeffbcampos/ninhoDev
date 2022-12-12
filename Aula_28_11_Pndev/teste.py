def calc():
    
    n1 = input("Digite o primeiro numero: ")
    op = input("Digite o operador (+, -, *, /, **, %(raiz)): ")
    if op == '%':
        res = float(n1) ** 0.5
        print(res)
    else:
        n2 = input("Digite o segundo numero: ")    
        res = eval(n1+op+n2)
        print(res)
    while True:
        op = input("Digite o operador (+, -, *, /, **, ): ")
        n3 = input("Digite um numero: ")
        res = eval(str(res)+ op +n3)
        print(res)
print(calc())





