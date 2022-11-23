# Faça uma função que receba uma lista de números armazenados de forma crescente, e
# dois valores ( limite inferior e limite superior), e exiba a sublista cujos elementos são
# maiores ou iguais ao limite inferior e menores ou iguais ao limite superior.

lista = []

for i in range(10):
    lista.append(int(input("Digite um número para lista: ")))
lista.sort()

print(f"A ordem crescente da lista é {lista}")

def limite(lista, menor, maior):
    newLista = []
    for i in range(len(lista) - 1):
        if lista[i] >= menor and lista[i ]<= maior:
            newLista.append(lista[i])       
    newLista.sort()
    return newLista


menor = int(input("Digite o limite menor: "))
maior = int(input("Digite o limite maior: "))


print(limite(lista, menor, maior))
#teste