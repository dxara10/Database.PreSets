import psycopg2

def conectar_postgresql(host, usuario, senha, banco_dados):
    return psycopg2.connect(
        host=host,
        user=usuario,
        password=senha,
        database=banco_dados
    )

def consultar_postgresql(conexao, query, parametros=None):
    cursor = conexao.cursor()
    if parametros:
        cursor.execute(query, parametros)
    else:
        cursor.execute(query)
    resultado = cursor.fetchall()
    cursor.close()
    return resultado
