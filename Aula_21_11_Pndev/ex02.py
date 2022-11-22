#Escreva um programa em Python para somar todos os itens de uma lista.

#Sem entradas do usuário:

listaNums = [1, 2, 3, 4]
print(f"A soma dos números da lista é {sum(listaNums)}")

#Com entradas do usuário: 

listaNums = []

for i in range(5):
    listaNums.append(int(input("Digite os numeros que deseja somar: ")))

print(f"A soma dos números da lista é {sum(listaNums)}")

