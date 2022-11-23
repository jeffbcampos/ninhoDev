# Crie uma função que permita contar o número de vezes que aparece uma letra em uma
# string.

def numletras(word, letra):
    total = word.count(letra)
    return(total)

palavra = input("Digite uma palavra: ")
letra = input("Digite a letra que será contada: ")

print(f"A letra {letra} aparece {numletras(palavra, letra)} vezes")
