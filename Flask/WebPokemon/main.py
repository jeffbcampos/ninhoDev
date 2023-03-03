from flask import Flask, render_template, request,flash, redirect,url_for
import psycopg2
from Controle.classConexao import Conexao
from Modelo.classPokemon import Pokemon

con = Conexao("pokedexapi", "localhost", "5432", "postgres", "postgres")
app = Flask(__name__)
app.config['SECRET_KEY'] = "12314124" 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Pokemons")
def verPokemons():
    resultado = con.consultarBanco('''Select * FROM "Pokemons"
     ''')   

    if "Ocorreu um erro" in resultado:
        return resultado
    else:
        return render_template("pokemons.html", pokemons=resultado) 



@app.route("/Pokemons/Inserir", methods=("GET","POST"))
def inserirPokemons():
    if request.method == "POST":

        pokemon = Pokemon(None,None,None,None,None)

        pokemon._id = request.form['id']
        pokemon._especie = request.form['nome']
        pokemon._peso = request.form['peso']
        pokemon._altura = request.form['altura']
        pokemon._tipo = request.form['tipo']

        resultado = con.manipularBanco(pokemon.sqlInserirPokemon())

        if "Deu certo" == resultado:

            return redirect(url_for('inserirPokemons'))
        else:
            return resultado


    else:
        return render_template("inserirpokemons.html")

if __name__ == "__main__":
    app.run(debug=True)

