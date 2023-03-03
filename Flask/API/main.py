from flask import Flask, jsonify
from Controle.classConexao import Conexao
from Modelo.classPokemon import Pokemon

con = Conexao("pokedexapi", "localhost", "5432", "postgres", "postgres")

app = Flask(__name__)

@app.route('/')
def home():
    return "API está rodando"

@app.route('/Pokemons')
def verPokemons():
    resultado = con.consultarBanco('''SELECT * FROM "Pokemons"''')
    
    if "erro" in resultado:
        return "Ocorreu um erro"
    
    else:
        return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)