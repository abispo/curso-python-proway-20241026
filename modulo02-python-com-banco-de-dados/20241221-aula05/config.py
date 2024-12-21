import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carrega os dados do arquivo .env e cria variáveis de ambiente a partir desses dados
load_dotenv()

# Lemos o valor da variável de ambiente 'DATABASE_URL' e salvamos na variável connection_string
connection_string = os.getenv("DATABASE_URL")

# Criamos a conexão com o banco de dados a partir da connection string. O parâmetro 'echo=True' faz os comandos SQL que serão executados, serem exibidos no terminal. Isso é muito útil para fins de depuração.
connection = create_engine(connection_string, echo=True)