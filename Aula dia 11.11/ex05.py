name = input("Digite o seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if(media >= 7):
    print(f"Parabéns {name}: Você foi aprovado")
elif(media <= 5):
    print(f"Ah {name}, você foi reprovado :( -- Melhor estudar mais!")
else:
    print(f"Vamos lá {name}, você ficou de recuperação, mas da pr recuperar. Estude!")


