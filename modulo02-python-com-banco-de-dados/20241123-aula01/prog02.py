# 1. Importar os módulos/pacotes da biblioteca padrão
# 2. Importar os módulos/pacotes instalados via pip
# 3. Importar os módulos/pacotes do próprio projeto

import csv
import os

import pymysql
import pymysql.cursors
import requests

if __name__ == "__main__":
    
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="admin",
        database="modulo02_python",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor  # Retora uma lista de dicionários como resposta
    )

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS tb_cursos;")

    comando = """
        CREATE TABLE tb_cursos(
            id INT PRIMARY KEY AUTO_INCREMENT,
            curso VARCHAR(100) NOT NULL,
            carga_horaria TINYINT UNSIGNED NOT NULL,
            preco FLOAT NOT NULL
        );
"""

    cursor.execute(comando)

    # URL de onde o conteúdo será baixado
    url_arquivo_cursos = "https://raw.githubusercontent.com/abispo/shared-files/refs/heads/main/modulo02/cursos.csv"

    # O método get da biblioteca requests acessa um endpoint (endereço) e baixa o seu conteúdo, independente de qual conteúdo seja
    resposta = requests.get(
        url_arquivo_cursos
    )

    pasta_arquivos = os.path.join(os.getcwd(), "arquivos")

    if not os.path.exists(pasta_arquivos):
        os.mkdir(pasta_arquivos)

    with open(os.path.join(pasta_arquivos, "cursos.csv"), "w", encoding="utf-8") as arquivo:
        arquivo.write(resposta.text)

    with open(os.path.join(pasta_arquivos, "cursos.csv"), "r", encoding="utf-8") as arquivo:

        arquivo_csv = csv.DictReader(arquivo, delimiter=';')

        for linha in arquivo_csv:
            comando = "INSERT INTO `tb_cursos` (`curso`, `carga_horaria`, `preco`) VALUES (%s, %s, %s);"
            cursor.execute(
                comando,
                (
                    linha.get("curso"),
                    int(linha.get("carga_horaria")),
                    float(linha.get("preco")),
                )
            )

            connection.commit()

    comando = "SELECT * FROM tb_cursos"
    cursor.execute(comando)
    print(cursor.fetchall())