import requests

def verPokemons():
    print("Viu")

resposta = requests.get("http://127.0.0.1:5000/Pokemons").json()

print(resposta)

print('''
      Bem vindo ao programa pokemon:
      1- Ver pokemons
      2- Inserir Pokemons
      3- Deletar Pokemons
      4- Modificar Pokemons
      ''')

opcao = input()

match opcao:
    case '1':
        verPokemons()
    case _:
        print("Opcao Invalida")
        