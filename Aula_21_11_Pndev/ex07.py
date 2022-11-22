#Escreva um programa Python para contar o número de strings em que o comprimento da string é 2 ou mais e o primeiro e o último caractere são iguais em uma determinada lista de strings.

words = ['abc', 'xyz', 'aba', '1221', 'agua']
contador = 0

for i in range(len(words)):
    if(words[i][0] == words[i][len(words[i]) - 1]):
        contador += 1
print(contador)

