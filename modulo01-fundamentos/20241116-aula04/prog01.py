"""
Entrada e Saída (I/O) de arquivos em Python

Leitura de arquivos .txt
"""

import os

if __name__ == "__main__":
    
    """
    Aqui utilizamos a função join do pacote os.path. Essa função é bastante útil quando queremos indicar o caminho de um arquivo, independentemente da plataforma onde nosso código está rodando (windows, linux, mac, etc).

    Basicamente, a função join combina caminhos indicados, e forma um caminho completo. No caso abaixo, o resultado da função os.getcwd() é concatenado com "arquivos" e que é concatenado com "linguagens.txt".

    os.getcwd() retorna o caminho completo de onde o script está sendo executado. Ou seja, caso o script esteja sendo executado em C:\\scripts\\prog01.py, a variável caminho arquivo irá ter o seguinte conteúdo:

    C:\\scripts\\arquivos\\linguagens.txt
    """
    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "linguagens.txt")

    """
    A função built-in open() é a responsável por carregar esse arquivo. Podemos abrir qualquer tipo de arquivo com o Python, tanto arquivos texto comuns (.txt, csv, .html, etc) quanto arquivos binários (.png, .exe, .mp3, etc)

    No caso abaixo, estamos passando apenas o parâmetro obrigatório dessa função, que é o caminho onde está o arquivo. Portanto, a função open() vai assumir que está sendo carregado um arquivo de texto plano, no modo somente-leitura
    """
    arquivo = open(file=caminho_arquivo)
    print(arquivo.read())
    arquivo.close()
