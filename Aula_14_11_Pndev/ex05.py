n1 = float(input("Digite a 1º nota: "))
n2 = float(input("Digite a 2º nota: "))
n3 = float(input("Digite a 3º nota: "))
n4 = float(input("Digite a 4º nota: "))

media = (n1 + n2 + n3 + n4) / 4

if(media >= 5):
    print(f"O aluno foi aprovado com media {media:.1f}")
else:
    print(f"O aluno não foi aprovado com média {media:.1f}")
