from random import randint

class Pokemon:
    def __init__(self, nome, tipo, ataque, hp):
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.hp = hp
    
    def atacar(self, pokemon):
        sorte = randint(1, 5)
        sorteInimigo = randint(1, 5)
        if sorte >= sorteInimigo:
            print(f"{self.nome} atacou {pokemon.nome}!")
            if self.tipo == "fogo":
                if pokemon.tipo == "fogo":
                    pokemon.hp -= self.ataque
                elif pokemon.tipo == "agua":
                    pokemon.hp -= self.ataque * 0.5
                elif pokemon.tipo == "grama":
                    pokemon.hp -= self.ataque * 2
                else:
                    pokemon.hp -= self.ataque
            elif self.tipo == "agua":
                if pokemon.tipo == "fogo":
                    pokemon.hp -= self.ataque * 2
                elif pokemon.tipo == "agua":
                    pokemon.hp -= self.ataque
                elif pokemon.tipo == "grama":
                    pokemon.hp -= self.ataque * 0.5
                else:
                    pokemon.hp -= self.ataque
            elif self.tipo == "grama":
                if pokemon.tipo == "fogo":
                    pokemon.hp -= self.ataque * 0.5
                elif pokemon.tipo == "agua":
                    pokemon.hp -= self.ataque * 2
                elif pokemon.tipo == "grama":
                    pokemon.hp -= self.ataque
                else:
                    pokemon.hp -= self.ataque
            else:
                pokemon.hp -= self.ataque
        else:
            print("O ataque falhou!")

def batalhaPokemon(pokemon1, pokemon2):
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        opcao = input(f"Digite 1 para {pokemon1.nome} atacar {pokemon2.nome}\nDigite 2 para {pokemon2.nome} atacar {pokemon1.nome}\n")
        if opcao == "1":
            pokemon1.atacar(pokemon2)
        elif opcao == "2":
            pokemon2.atacar(pokemon1)
        else:
            print("Opção inválida!")
        print(f"{pokemon1.nome} HP: {pokemon1.hp}")
        print(f"{pokemon2.nome} HP: {pokemon2.hp}")
    if pokemon1.hp <= 0:
        print(f"{pokemon1.nome} foi derrotado!")
    elif pokemon2.hp <= 0:
        print(f"{pokemon2.nome} foi derrotado!")

pokemon1 = Pokemon("Charmander", "fogo", 10, 100)
pokemon2 = Pokemon("Squirtle", "agua", 10, 100)

# pokemon1 = input("Digite o nome do primeiro pokemon: ")
# tipo1 = input("Digite o tipo do primeiro pokemon: ")
# ataque1 = int(input("Digite o ataque do primeiro pokemon: "))
# hp1 = int(input("Digite o HP do primeiro pokemon: "))
# pokemon2 = input("Digite o nome do segundo pokemon: ")
# tipo2 = input("Digite o tipo do segundo pokemon: ")
# ataque2 = int(input("Digite o ataque do segundo pokemon: "))
# hp2 = int(input("Digite o HP do segundo pokemon: "))
# pokemon1 = Pokemon(pokemon1, tipo1, ataque1, hp1)
# pokemon2 = Pokemon(pokemon2, tipo2, ataque2, hp2)

batalhaPokemon(pokemon1, pokemon2)

        