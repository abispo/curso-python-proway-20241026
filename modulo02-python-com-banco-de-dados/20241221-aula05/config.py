import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, DeclarativeBase

# Carrega os dados do arquivo .env e cria variáveis de ambiente a partir desses dados
load_dotenv()

# Lemos o valor da variável de ambiente 'DATABASE_URL' e salvamos na variável connection_string
connection_string = os.getenv("DATABASE_URL")

# Criamos a conexão com o banco de dados a partir da connection string. O parâmetro 'echo=True' faz os comandos SQL que serão executados, serem exibidos no terminal. Isso é muito útil para fins de depuração.
connection = create_engine(connection_string, echo=True)

# Abaixo, criamos uma sessão de acesso ao banco de dados. É a partir desse objeto que os comandos serão executados no banco de dados.
session = scoped_session(sessionmaker(
    bind=connection, autoflush=False
))

# Classe base para todas as models. Se quisermos que uma classe seja mapeada para uma tabela no banco de dados, devemos obrigatoriamente fazê-la herdar da classe Base, que por sua vez herda da classe DeclarativeBase
class Base(DeclarativeBase):
    pass
