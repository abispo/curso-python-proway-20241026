"""
Entrada e Saída (I/O) de arquivos em Python

Trabalhando com arquivos csv (Comma Separated Values|Valores Separados por Vírgula)

Lendo um arquivo .csv com reader e DictReader()
"""

import csv
import os

def exibir_info(nome: str, idade: str, valor: str):
    # O método de strings ljust justifica a esquerda um texto, e preenche com espaços vazios o restante
    print("{} {} {}".format(
        nome.ljust(10), idade.ljust(5), valor.rjust(10)
    ))

if __name__ == "__main__":
    
    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "clientes.csv")
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

        """
        Aqui criamos um objeto do tipo csv.reader. Nesse caso, as linhas do arquivo serão lidas como listas de valores, onde cada coluna do arquivo .csv será um valor.

        Passamos o parâmetro delimiter, pois por padrão o Python entende que um arquivo .csv é separado por vírgulas. No nosso caso, estamos separando as colunas do nosso arquivo com ponto-e-vírgula.
        """
        arquivo_csv = csv.reader(arquivo, delimiter=';')

        """
        A única maneira de lermos um arquivo csv, é passando ele para um laço for. O laço for será executado enquanto houverem linhas a serem lidas no arquivo.

        A função enumerate retorna o índice de leitura e o objeto lido. No caso abaixo, ele irá começar do número 1 i irá iterando esse número até o final do arquivo.
        """
        for i, linha in enumerate(arquivo_csv, start=1):
            # Essa condição existe para não ser exibida a primeira linha do arquivo
            if i != 1:
                exibir_info(*linha)

        print('-'*50)
        
        # DictReader
        with open(caminho_arquivo, 'r', encoding="utf-8") as arquivo:

            arquivo_csv = csv.DictReader(arquivo, delimiter=';')

            for linha in arquivo_csv:
                exibir_info(**linha)