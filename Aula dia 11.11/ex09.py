# 3.Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.

listaNumeros = []
n = 0

for i in range(6):
    n = int(input("Digite um numero: "))
    listaNumeros.append(n)
print(f"O numero menor digitado foi {min(listaNumeros)}")