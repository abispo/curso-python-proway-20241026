"""
Python com banco de dados

Assim como em outras linguagens, podemos acessar bancos de dados utilizando Python. Isso é feito por meio de bibliotecas de acesso, que podemos também chamar de conector.

Por padrão, o Python já vem com uma biblioteca para trabalhar com bancos de dados do tipo SQLite.
"""

import os
import sqlite3

if __name__ == "__main__":
    """
    Para trabalhar com bancos de dados em Python utilizando os conectores, seguimos a seguinte ordem:

    1. Definimos a connection string do banco. Connection string basicamente é um texto com todas as informações para acesso ao banco de dados (usuario, senha, servidor, porta, banco, etc).
    2. Criamos uma conexão com o banco de dados, a partir dessa connection string.
    3. Criamos um cursor a partir da conexão, onde poderemos executar os código SQL
    4. Recebemos os resultados dos comandos (se necessário)
    """

    # 1. Criamos a connection string. No caso do SQLite, definimos o nome que o arquivo que representa o banco de dados terá
    connection_string = os.path.join(os.getcwd(), "db.sqlite3")

    # 2. Criamos a conexão com o banco a partir da connection string
    connection = sqlite3.connect(connection_string)

    # 3. Criamos o cursor a partir da conexão
    cursor = connection.cursor()

    # Criação da tabela tb_alunos. A cada vez que o script rodar, essa tabela será zerada. Os comandos sempre serão strings. As strings devem ser comandos SQL válidos.
    comando = "DROP TABLE IF EXISTS tb_alunos"
    cursor.execute(comando)

    comando = """
        CREATE TABLE tb_alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
            curso TEXT NOT NULL
        );
    """

    # Execução do comando
    cursor.execute(comando)

    lista_alunos = [
        {"nome": "Maria", "cidade": "Blumenau", "curso": "Python"},
        {"nome": "Josefa", "cidade": "Indaial", "curso": "Python"},
        {"nome": "Jorge", "cidade": "Brusque", "curso": "Java"},
        {"nome": "Vitor", "cidade": "Blumenau", "curso": "Java"},
        {"nome": "Bruna", "cidade": "Pomerode", "curso": "PHP"},
    ]

    for aluno in lista_alunos:
        comando = """
            INSERT INTO tb_alunos(nome, cidade, curso) VALUES(
                '{nome}', '{cidade}', '{curso}'
            );
    """.format(**aluno)
        
        cursor.execute(comando)

        # Apenas a linha acima não salva os dados na tabela, pois quando utilizamos comandos do tipo DML (INSERT, UPDATE e DELETE), precisamos confirmar essa transação. Para isso, utilizamos o método commit() da conexão.
        # É possível salvar os dados apenas no final dos INSERTs. Para isso, coloque a chamada ao método commit fora do laço for
        connection.commit()

    # Para trazer os dados das consultas, utilizamos o comando SELECT. Podemos trazer os resultados desse comando utilizando 3 métodos diferentes
    comando = "SELECT * FROM tb_alunos;"
    resultado = cursor.execute(comando)

    # fetchone() -> Traz apenas 1 registro da consulta. Se a consulta não trouxe resultados, retorna None. Caso haja resultados, o fetchone() retornará uma tupla. A ordem dos elementos é a mesma das colunas
    aluno = resultado.fetchone()
    print(f"Resultado com fetchone() {aluno}.")

    # fetchmany(qtd) -> Traz a quantidade indicada de registros da consulta. Se a consulta não trouxe resultados, retorna uma lista vazia
    alunos = resultado.fetchmany(2)
    print(f"Resultado com fetchmany(2): {alunos}")

    # fetchall() -> Traz todos os registros da consulta. Se a consulta não trouxer resultados, retorna uma lista vazia
    mais_alunos = resultado.fetchall()
    print(f"Resultado com fetchall(): {mais_alunos}")

    # Atualização de registro
    # Altera o valor da coluna curso para C# para todos os registros que tem a coluna cidade igual a Blumenau
    comando = "UPDATE tb_alunos SET curso = 'C#' WHERE cidade = 'Blumenau';"
    cursor.execute(comando)
    connection.commit()

    # Apagar registros
    # Apaga todas as linhas que tenham a coluna Curso igual a Java
    comando = "DELETE FROM tb_alunos WHERE curso = 'Java';"
    cursor.execute(comando)
    connection.commit()
