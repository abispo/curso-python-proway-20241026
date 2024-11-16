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

    No caso abaixo, estamos passando apenas o parâmetro obrigatório dessa função, que é o caminho onde está o arquivo. Portanto, a função open() vai assumir que está sendo carregado um arquivo de texto plano, no modo somente-leitura.

    Podemos indicar o modo de abertura do arquivo, ou seja, o que pretendemos fazer. Os modos de abertura mais comuns são os seguintes:

        r (read|leitura)        -> Abre o arquivo no modo somente-leitura, ou seja, não conseguimos fazer modificações. Caso não indiquemos o modo, esse será o padrão.
        w (write|escrita)       -> Abre o arquivo no modo de escrita. Caso o arquivo não exista, ele é criado. Caso o arquivo já exista, todo o seu conteúdo é apagado e substituído por um novo.
        a (append|acrescentar)  -> Abre o arquivo no modo acrescentar. Caso o arquivo não exista, ele é criado. Caso o arquivo já exista, ele acrescenta o conteúdo a partir do final do arquivo.

    Também podemos indicar o tipo de arquivo que está sendo aberto:
        t (text|texto)      -> Arquivo de texto comum
        b (binary|binário)  -> Arquivo binário.

    Indicamos o tipo de arquivo junto com o modo de leitura. Por exemplo, se quisermos abrir um arquivo binário somente escrita, temos que passar o modo 'wb'. Caso não seja indicado o tipo de arquivo, o open irá assumir que está sendo aberto um arquivo texto.

    Além disso, podemos misturar os modos de abertura. Por exemplo, se quisermos abrir um arquivo para leitura e escrita ao mesmo tempo, podemos utilizar o modo 'r+' ou 'w+'
    """
    arquivo = open(file=caminho_arquivo)

    """
    Quando abrimos um a
    """
    print(arquivo.read())
    arquivo.close()
