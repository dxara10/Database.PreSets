import pyodbc

def conectar_sql_server(servidor, banco_dados, usuario, senha):
    conexao_str = f'DRIVER={{SQL Server}};SERVER={servidor};DATABASE={banco_dados};UID={usuario};PWD={senha}'
    return pyodbc.connect(conexao_str)

def consultar_sql_server(conexao, query):
    cursor = conexao.cursor()
    cursor.execute(query)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado
