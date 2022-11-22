#Escreva um programa em Python para multiplicar todos os itens de uma lista.

listaNums = [1, 2, 3, 4]
prod = 1

for i in listaNums:
    prod *= listaNums[i - 1]
print(f"O produto dos números da lista é {prod}")