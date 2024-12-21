from sqlalchemy import select

from config import session
from mensagens import MENU_USUARIOS
from models import Usuario, Perfil

def selecionar_usuarios():

    # comando = "SELECT usuarios.id, usuarios.email, usuarios.senha FROM usuarios;"
    comando = select(Usuario)

    # result = cursor.execute(comando).fetchall()
    result = session.execute(comando).scalars()

    # O método scalars() retorna um objeto iterável, que não traz todas as linhas da consulta de uma vez só. Esses resultados serão trazidos quando iterarmos esse objeto. Caso queiramos trazer o resultado como uma lista de objetos, devemos utilizar o método .all() logo após o .scalars()
    # result = session.execute(comando).scalars().all()

    # for usuario in result
    for usuario in result:
        print(f"E-mail: {usuario.email}.")
    
        # Pegar os dados de perfil
        # A função select retorna um objeto do tipo Select, que por sua vez tem um método chamado where(). No where passamos as condições para o retorno dos dados. No caso abaixo, a consulta trará todas as linhas da tabela perfis que tenham o id igual ao valor do atributo id do objeto Usuario atual.
        # Como estamos tratando de um relacionamento 1:1, utilizamos o método scalar_one(), que trará apenas 1 linha do resultado.
        # perfil = session.execute(
        #     select(Perfil).where(Perfil.id == usuario.id)
        # ).scalar_one()

        print(f"Nome: {usuario.perfil.nome} {usuario.perfil.sobrenome}")
        print(f"Data de Nascimento: {usuario.perfil.data_de_nascimento}")
        print('*'*50)

def inserir_usuario(email, senha, nome, sobrenome, data_de_nascimento) -> None:
    # Para inserção de um dado na tabela, precisamos instanciar a model, informando os valores dos seus atributos
    usuario = Usuario(email=email, senha=senha)
    
    # Após isso, adicionamos o objeto instanciado na sessão. É importante reforçar que nesse momento os dados ainda não foram salvos fisicamente na tabela, portanto, podem receber um comando de rollback (desfazer). Caro desejarmos adicionar mais de 1 objeto ao mesmo tempo, podemos utilizar o método add_all, que recebe uma lista de objetos
    session.add(usuario)

    # O método commit() do objeto session, pega todos os objetos que foram adicionados à sessão e os persiste (salva/atualiza) nas suas tabelas correspondentes
    session.commit()

    # Salvando os dados do perfil associado a esse usuário
    perfil = Perfil(
        id=usuario.id,
        nome=nome,
        sobrenome=sobrenome,
        data_de_nascimento=data_de_nascimento
    )
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
                selecionar_usuarios()

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
                    data_de_nascimento=data_de_nascimento if data_de_nascimento else None
                )

                print("USUÁRIO SALVO COM SUCESSO!")
