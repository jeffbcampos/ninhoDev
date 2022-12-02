p = 0

s = input("Digite o seu sexo F ou M: ").upper()

a = float(input("Digite sua altura: "))

if(s == 'F'):
    p = (62.1 * a) - 44.7
    print(f"Seu peso ideal é {p:.1f}")
elif(s == 'M'):
    p = (72.7 * a) - 58
    print(f"Seu peso ideal é {p:.1f}")
else:
    print("Digite um sexo válido")



