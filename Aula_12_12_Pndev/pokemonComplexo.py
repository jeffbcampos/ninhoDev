class Pokemon:
    def __init__(self, nome, tipo, hp):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.status = 'vivo'

def choosePokemon():
    print('Escolha seu pokemon:')
    print('1 - Pikachu')
    print('2 - Charmander')
    print('3 - Squirtle')
    print('4 - Bulbasaur')
    escolha = int(input('Digite o número do pokemon: '))
    if escolha == 1:
        return Pokemon('Pikachu', 'Elétrico', 100)
    elif escolha == 2:
        return Pokemon('Charmander', 'Fogo', 100)
    elif escolha == 3:
        return Pokemon('Squirtle', 'Água', 100)
    elif escolha == 4:
        return Pokemon('Bulbasaur', 'Planta', 100)
    else:
        print('Opção inválida')
        return choosePokemon()

player1 = choosePokemon()
player2 = choosePokemon()

def batalhaPokemon(pokemon1, pokemon2):
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        acao = print("O que você deseja fazer?")
        print("1 - Atacar")
        print("2 - Defender")
        acao = int(input("Digite o número da ação: "))
        if acao == 1:
            pokemon2.hp -= 10
            print(f"{pokemon1.nome} atacou {pokemon2.nome} e causou 10 de dano")
        elif acao == 2:
            pokemon1.hp += 10
            print(f"{pokemon1.nome} defendeu e recuperou 10 de HP")
        else:
            print("Ação inválida")
            continue
        if pokemon2.hp <= 0:
            pokemon2.status = 'morto'
            print(f"{pokemon2.nome} está morto")
            break
        print(f"{pokemon1.nome} tem {pokemon1.hp} de HP")
        print(f"{pokemon2.nome} tem {pokemon2.hp} de HP")
        print("Agora é a vez do outro jogador")
        acao = print("O que você deseja fazer?")
        print("1 - Atacar")
        print("2 - Defender")
        acao = int(input("Digite o número da ação: "))
        if acao == 1:
            pokemon1.hp -= 10
            print(f"{pokemon2.nome} atacou {pokemon1.nome} e causou 10 de dano")
        elif acao == 2:
            pokemon2.hp += 10
            print(f"{pokemon2.nome} defendeu e recuperou 10 de HP")
        else:
            print("Ação inválida")
            continue
        if pokemon1.hp <= 0:
            pokemon1.status = 'morto'
            print(f"{pokemon1.nome} está morto")
            break
        print(f"{pokemon1.nome} tem {pokemon1.hp} de HP")
        print(f"{pokemon2.nome} tem {pokemon2.hp} de HP")
        print("Agora é a vez do outro jogador")

batalhaPokemon(player1, player2)


        

