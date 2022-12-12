notas = []
soma = 0
maior_nota = []

for i in range(5):
    notas.append(int(input("Digite às 5 notas: ")))    
    soma += notas[i]    
media = soma / 5

for i in range(5):    
    if(notas[i] > media):
        maior_nota.append(notas[i])
    
print(f"Os valores maiores que a media são {maior_nota}")
print(f"A soma das notas é {soma}")
print(f"A media das notas é {media}")
