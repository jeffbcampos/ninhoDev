maior = []

n = int(input("Digite um numero maior que zero: "))

for i in range(n, -1, -1):
    maior.append(int(input("Digite um numero maior que zero: ")))
print(f"O maior numero é: {max(maior)}")