n = float(input("Digite um número: "))
a = 0
b = 0

if(n >= 0):
    a = n
    print(f"O número {a:.1f} é variável de A")
else:
    b = n
    print(f"O número {b:.1f} é variável de B")