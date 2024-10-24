from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def criar_sessao_sqlalchemy(host, usuario, senha, banco_dados):
    engine = create_engine(f'mysql://{usuario}:{senha}@{host}/{banco_dados}')
    Session = sessionmaker(bind=engine)
    return Session()
