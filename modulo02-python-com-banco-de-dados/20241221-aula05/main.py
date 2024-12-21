
from config import connection
from models import *

if __name__ == "__main__":
    # O comando abaixo utiliza o objeto de conexão para criar as tabelas associadas as classes
    Base.metadata.create_all(connection)