#Escreva um programa Python para contar o número de caracteres em uma string.

numCaract = {}
separ = []

word = input("Digite uma palavra para contar suas letras: ")

for i in range(len(word)):
    separ.append(word[i])

for i in range(len(separ)):
    numCaract[separ[i]] = separ.count(separ[i])
print(numCaract)

