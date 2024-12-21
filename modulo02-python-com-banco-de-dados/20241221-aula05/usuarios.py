from sqlalchemy import select

from config import session
from mensagens import MENU_USUARIOS
from models import Usuario, Perfil

def gerenciar_usuarios():
    
    while True:
        print(MENU_USUARIOS)
        opcao = int(input("Informe a opção desejada: "))

        match opcao:
            case 1:
                print("VOLTANDO AO MENU PRINCIPAL...")
                break
