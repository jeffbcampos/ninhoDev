from faker import Faker
import psycopg2
from psycopg2 import connect
from psycopg2 import Error

fake = Faker(['pt-BR'])

# for i in range(10):
#     print(f"Nome: {fake.name()} - Email: {fake.email()} - CPF: {fake.cpf()} - Telefone: {fake.phone_number()} - Data de Nascimento: {fake.date_of_birth(minimum_age=18, maximum_age=65)}")

def connection_db(host_name, user_name, pwd, db):
    connection = None
    try:
        connection = connect(
            host = host_name,
            user = user_name,
            password = pwd,
            database = db
        )
        print("Conexão Realizada com Sucesso")
    except Error as err:
        print(f"Error: '{err}'")
    
    return connection

con = connection_db("localhost", "postgres", "postgres", "BancoNinho")

cursor = con.cursor()

for i in range(15):
    cursor.execute(f'''
    INSERT INTO Alunos2 
    VALUES  (
        DEFAULT,
        '{fake.name()}',
        '{fake.cpf()}',
        '{fake.date_of_birth(minimum_age=18, maximum_age=65)}',
        '{fake.address()}',
        '{fake.cellphone_number()}'
    );''')
    

con.commit()    
