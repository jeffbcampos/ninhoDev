
palavra = input("Digite uma palavra: ")
letra = input("Digite a letra a ser contada: ")

contador = 0
for i in range(len(palavra)):
    if palavra[i] ==  letra:
        contador += 1

print(contador)