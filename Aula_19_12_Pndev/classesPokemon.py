class Pokemon:
    def __init__(self, nome, level):
        self.nome = nome
        self._level = level
        self.tipo = 'Normal'

    def checarVantagem(self, pokemonInimigo):
        if pokemonInimigo.tipo == 'Normal':
            print("A batalha deu empate")
        elif pokemonInimigo.tipo == 'Aquatico':
            print(f"O pokemon {self.nome} pedeu para {pokemonInimigo.nome}")
        elif pokemonInimigo.tipo == 'Grama':
            print(f"O pookemon {self.nome} venceu o pokemon {pokemonInimigo.nome}")
        else:
            print(f"Não foi possivel identificar o vencedor")

class PokemonAquatico(Pokemon):
    def __init__(self, nome, level):
        super().__init__(nome, level)
        self.tipo = 'Aquatico'

    def checarVantagem(self, pokemonInimigo):
        if pokemonInimigo.tipo == 'Normal':
            print(f"o pokemon {self.nome} ganhou do pokemon {pokemonInimigo.nome}")
        elif pokemonInimigo.tipo == 'Eletrico':
            print(f"O pokemon {self.nome} perdeu para {pokemonInimigo.nome}")
        elif pokemonInimigo.tipo == 'Grama':
            print(f"O pookemon {self.nome} venceu o pokemon {pokemonInimigo.nome}")
        else:
            print(f"Não foi possivel identificar o vencedor")

porigon = Pokemon('Porygon', 12)
squirtle = PokemonAquatico('Sqirtle', 20)

porigon.checarVantagem(squirtle)
squirtle.checarVantagem(porigon)