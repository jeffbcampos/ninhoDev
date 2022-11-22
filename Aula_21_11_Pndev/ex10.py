#Escreva um programa Python para construir o seguinte padrão, usando um loop for aninhado.

caract = '*'

for i in range(1, 5):
    print(caract)
    caract += '*'
for i in range(6, -1, -1):
    print(caract)
    caract = '*' * i