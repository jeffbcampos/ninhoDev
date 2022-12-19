class Pokemon:
    def __init__(self, nome, tipo, forca, hp):
        self.nome = nome
        self.tipo = tipo
        self.forca = forca
        self.hp = hp

    def atacar(self, pokemon):
        if self.tipo == 'fogo':
            if pokemon.tipo == 'fogo':
                pokemon.hp -= self.forca
            elif pokemon.tipo == 'agua':
                pokemon.hp -= self.forca / 2
            elif pokemon.tipo == 'grama':
                pokemon.hp = pokemon.hp - self.forca * 2            
        elif self.tipo == 'agua':
            if pokemon.tipo == 'fogo':
                pokemon.hp -= (self.forca * 2)
            elif pokemon.tipo == 'grama':
                pokemon.hp -= self.forca / 2
            elif pokemon.tipo == 'fogo':
                pokemon.hp -= self.ataque            


def batalhaPokemon(pok1, pok2):
    while pok1.hp > 0 and pok2.hp > 0:
        atk = input(f"Digite qual pokemon ai atacar:\n1- {pok1.nome}\n2-{pok2.nome}\n")
        opcao = input("Digite o que quer:\n1- Atacar\n2-Passar a vez\n")
        if atk == '1' and opcao == '1':
            pok1.atacar(pok2)
            print(f"{pok1.nome} atacou {pok2.nome}!")
            print(f"HP {pok2.nome}: {pok2.hp}")
        elif atk == '2' and opcao == '1':
            pok2.atacar(pok1)
            print(f"{pok2.nome} atacou {pok1.nome}!")
            print(f"HP {pok1.nome}: {pok1.hp}")
        


charmander = Pokemon('Charmander', 'fogo', 10, 100)
squirtle = Pokemon('Squirtle', 'agua', 10, 100)

batalhaPokemon(charmander, squirtle)