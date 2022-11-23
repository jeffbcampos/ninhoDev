# 2.Ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.

num = []
n = 0
listaNumeros = []

for i in range(11):
   n = int(input("Digite um numero: "))
   num.append(n)
   if(n >= 10 and n <= 50):
    listaNumeros.append(n)

print(f"Os numeros digitados entre 10 e 50 são {listaNumeros}")
