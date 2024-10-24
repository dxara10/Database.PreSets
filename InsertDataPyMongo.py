from pymongo import MongoClient

def conectar_mongodb(host, porta, usuario, senha, banco_dados):
    cliente = MongoClient(host, porta, username=usuario, password=senha)
    return cliente[banco_dados]

def inserir_documento_mongodb(colecao, documento):
    return colecao.insert_one(documento)
