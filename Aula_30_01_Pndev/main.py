from psycopg2 import connect
from psycopg2 import Error

def connection(db_name):
    connection = None
    try:
        connection = connect(
            host = "localhost",
            user = "postgres",
            password = "postgres",
            database = db_name
        )
        print("Conexão Realizada")
    except Error as err:
        print(f"Error: {err}")

    return connection

con = connection("BancoNinho")

# query = '''
#     CREATE TABLE funcionarios (
#         id int GENERATED ALWAYS AS IDENTITY,
#         Nome VARCHAR(255),
#         Cpf CHAR(11),
#         Salário MONEY,
#         Dept_Id int,
#         CONSTRAINT fk_departamento
#             FOREIGN KEY(Dept_Id)
#             REFERENCES Departamentos(dept_id)
#             ON DELETE NO ACTION
#             ON UPDATE NO ACTION,
        
#         PRIMARY KEY (id)            
#             );'''

def queryExecute(query):
    cursor = con.cursor()
    cursor.execute(query)
    con.commit()
    cursor.close()
    con.close()

def querySelect(table, column, value):
    cursor = con.cursor()
    cursor.execute(f'''
        SELECT * from {table} WHERE {column} = '{value}';
    '''        
    )
    query = cursor.fetchall()
    cursor.close()
    con.close()
    return query

# func = querySelect('funcionarios', 'id', '3')[0]

# print(func)

cursor = con.cursor()

cursor.execute('''
    SELECT f.nome, f.salario, d.dept_nome as Departamento from funcionarios f inner join departamentos d on d.dept_id = f.dept_id; 
''')
func = cursor.fetchall()[0]

print(func)