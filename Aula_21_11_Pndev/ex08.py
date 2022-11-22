#Escreva um programa Python para adivinhar um número entre 1 a 9. Nota: O usuário é solicitado a inserir um palpite. Se o usuário adivinhar errado, o prompt aparecerá novamente até que o palpite esteja correto. Se o palpite for bem-sucedido, o usuário receberá um "Bem adivinhado!" mensagem e o programa será encerrado.


from random import randint
pc = randint(1, 10)
palpite = 0
jogador = 0
print('Olá, estou pensando em número entre 0 e 10. Você consegue adivinhar?')
while jogador != pc:
  jogador = int(input('Qual é o seu palpite: '))
  if jogador < pc:
    print('O número é maior... Tente novamente\n')
  elif jogador > pc:
    print('O número é menor... Tente novamente\n')
  palpite += 1
print(f'Parabéns! Você acertou com {palpite} palpites')