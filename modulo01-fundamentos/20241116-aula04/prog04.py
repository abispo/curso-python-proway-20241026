"""
Entrada e Saída (I/O) de arquivos em Python

Trabalhando com arquivos csv (Comma Separated Values|Valores Separados por Vírgula)

Escrevendo em um arquivo .csv com writer e DictWriter()
"""

import csv
import os

if __name__ == "__main__":
    
    lista_de_compras = [
        [1, "Pilha AAA", 2, 19.90],
        [2, "Fone de Ouvido", 1, 56.90],
        [3, "Teclado Gamer", 1, 111.90],
        [4, "Mousepad do Relâmpago McQueen", 9.90],
        [5, "Monitor Samsung", 1, 599.90]
    ]

    caminho_pasta_saida = os.path.join(os.getcwd(), "saida")

    if not os.path.exists(caminho_pasta_saida):
        os.mkdir(caminho_pasta_saida)

    caminho_arquivo = os.path.join(caminho_pasta_saida, "compras.csv")

    with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:

        arquivo_csv = csv.writer(arquivo, delimiter=';')

        # O método writerow grava uma linha no arquivo. Essa linha será uma lista
        arquivo_csv.writerow(["codigo", "produto", "quantidade", "valor"])
        
        # O método writerows grava várias linhas no arquivo de uma vez só. Ele recebe uma lista de listas
        arquivo_csv.writerows(lista_de_compras)

    lista_de_compras = [
        {"id": 1, "produto": "Pilha AAA", "quantidade": 2, "valor": 19.90},
        {"id": 2, "produto": "Fone de Ouvido", "quantidade": 1, "valor": 56.90},
        {"id": 3, "produto": "Teclado Gamer", "quantidade": 1, "valor": 111.90},
    ]

    with open(caminho_arquivo, "w", encoding="utf-8", newline="") as arquivo:

        arquivo_csv = csv.DictWriter(
            arquivo,
            # Indicamos as colunas passando uma lista para o parâmetro fieldnames
            fieldnames=["id", "produto", "quantidade", "valor"],
            delimiter=';'
        )

        # O método writeheader() salva as colunas no arquivo. Colunas que foram indicadas no parâmetro fieldnames do DictWriter
        arquivo_csv.writeheader()

        # Salva no arquivo os dados. Cada linha é um dicionário, que faz parte de uma lista de dicionários
        arquivo_csv.writerows(lista_de_compras)