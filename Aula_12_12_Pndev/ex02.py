def existeLetra():
    palavra = input('Digite uma palavra: ')
    letra = input('Digite uma letra: ')
    if letra in palavra:
        print('A letra existe na palavra')
    else:
        print('A letra não existe na palavra')


existeLetra()