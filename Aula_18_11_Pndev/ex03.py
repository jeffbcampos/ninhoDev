# Dada uma palavra, retorna os caracteres nas posições
# ímpares

word = input("Digite uma palavra: ")
#Oragotano
wordImpar = []

for i in range(0, len(word)):
    if(i % 2 != 0):
        wordImpar.append(word[i])

print(f"As letras nas posições ímpares são {wordImpar}")
