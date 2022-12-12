class Pokemon:
    def __init__(self, nome, tipo, nivel):
        self.nome = nome
        self.tipo = tipo
        self.nivel = nivel

pikachu = Pokemon('Pikachu', 'Elétrico', 21)
print(f"{pikachu.nome} é do tipo {pikachu.tipo} e está no nível {pikachu.nivel}")

venusaur = Pokemon('Venusaur', 'Planta', 42)
print(f"{venusaur.nome} é do tipo {venusaur.tipo} e está no nível {venusaur.nivel}")

def batalhaPokemon(pokemon1, pokemon2):
    if pokemon1.nivel > pokemon2.nivel:
        print(f"{pokemon1.nome} venceu a batalha")
    elif pokemon1.nivel < pokemon2.nivel:
        print(f"{pokemon2.nome} venceu a batalha")
    else:
        print('A batalha terminou empatada')

batalhaPokemon(pikachu, venusaur)