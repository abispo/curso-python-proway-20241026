
from config import connection
from models import *

from mensagens import MENU_PRINCIPAL
from usuarios import gerenciar_usuarios

if __name__ == "__main__":
    # O comando abaixo utiliza o objeto de conexão para criar as tabelas associadas as classes
    # Como estamos utilizando o SQLAlchemy para controlar as alterações no banco de dados, não precisamos mais do comando abaixo
    # Base.metadata.create_all(connection)

    while True:
        print(MENU_PRINCIPAL)
        opcao = int(input("Informe a opção desejada: "))

        match opcao:
            case 1:
                print("SAINDO...")
                break

            case 2:
                gerenciar_usuarios()