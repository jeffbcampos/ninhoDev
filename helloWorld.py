msg = "Este é um Texto"

palavras = msg.split()

print("A mensagem original é:", msg)
print("O resultado da função upper é:", msg.upper())
print("O resultado da função lower é:", msg.lower())
print("O resultado da função capitalize é:", msg.capitalize())
print("O resultado da função split é:", msg.split())
print("O resultado da função count é:", msg.lower().count('e'))
print("O tamanho do texto é:", len(msg))
print(f"O resultado da função upper é: {msg.upper()}")


def sum(a, b):
    n = a + b
    return print("A soma é", n)

sum(4, 5)
x = int(input("Digite: "))
print(x)