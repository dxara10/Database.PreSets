import sqlite3

def conectar_bd(nome_bd):
    conexao = sqlite3.connect(nome_bd)
    return conexao

def consultar_bd(conexao, query, parametros=None):
    cursor = conexao.cursor()
    if parametros:
        cursor.execute(query, parametros)
    else:
        cursor.execute(query)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado
