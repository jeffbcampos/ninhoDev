a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if(a > b and a > c and b > c):
    print(f"{a}, {b}, {c}")
elif(a > b and a > c and b < c):
    print(f"{a}, {c}, {b}")
elif(a < b and a < c and b > c):
    print(f"{b}, {c}, {a}")
elif(a < b and a > c):
    print(f"{b}, {a}, {c}")
elif(c > a and c > b and a > b):
    print(f"{c}, {a}, {b}")
elif(a > b and a > c):
    print(f"{a}, {b}, {c}")


 

 
