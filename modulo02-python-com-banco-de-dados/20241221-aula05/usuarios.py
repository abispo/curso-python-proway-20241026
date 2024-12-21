from sqlalchemy import select

from config import session
from mensagens import MENU_USUARIOS
from models import Usuario, Perfil

def inserir_usuario(email, senha, nome, sobrenome, data_de_nascimento) -> None:
    # Para inserção de um dado na tabela, precisamos instanciar a model, informando os valores dos seus atributos
    usuario = Usuario(email=email, senha=senha)
    
    # Após isso, adicionamos o objeto instanciado na sessão. É importante reforçar que nesse momento os dados ainda não foram salvos fisicamente na tabela, portanto, podem receber um comando de rollback (desfazer). Caro desejarmos adicionar mais de 1 objeto ao mesmo tempo, podemos utilizar o método add_all, que recebe uma lista de objetos
    session.add(usuario)

    # O método commit() do objeto session, pega todos os objetos que foram adicionados à sessão e os persiste (salva/atualiza) nas suas tabelas correspondentes
    session.commit()

    # Salvando os dados do perfil associado a esse usuário
    perfil = Perfil(nome=nome, sobrenome=sobrenome, data_de_nascimento=data_de_nascimento)
    session.add(perfil)
    session.commit()

def gerenciar_usuarios():
    
    while True:
        print(MENU_USUARIOS)
        opcao = int(input("Informe a opção desejada: "))

        match opcao:
            case 1:
                print("VOLTANDO AO MENU PRINCIPAL...")
                break

            case 2:
                pass

            case 3:
                email = input("Informe o e-mail do usuário: ")
                senha = input("Informa a senha do usuário: ")
                nome = input("Informe o primeiro nome do usuário: ")
                sobrenome = input("Informe o sobrenome do usuário: ")
                data_de_nascimento = input("Informe a data de nascimento do usuário (YYYY-MM-DD): ")

                inserir_usuario(
                    email=email,
                    senha=senha,
                    nome=nome,
                    sobrenome=sobrenome,
                    data_de_nascimento=data_de_nascimento
                )

                print("USUÁRIO SALVO COM SUCESSO!")
