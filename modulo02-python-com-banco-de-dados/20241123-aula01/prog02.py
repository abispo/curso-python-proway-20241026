import csv
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
        cursorclass=pymysql.cursors.DictCursor
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

    url_arquivo_cursos = "https://raw.githubusercontent.com/abispo/shared-files/refs/heads/main/modulo02/cursos.csvs"