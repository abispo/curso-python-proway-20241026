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

        r (read|leitura)        -> Abre o arquivo no modo somente-leitura, ou seja, não conseguimos fazer modificações. Caso não indiquemos o modo, esse será o padrão. Caso o arquivo não exista, é gerada uma exceção do tipo FileNotFoundError.
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
    Quando abrimos um arquivo no modo de leitura, recebemos um objeto que representa esse arquivo. Com isso, temos acesso a alguns métodos para a leitura do conteúdo do arquivo. No caso abaixo, chamamos o método read(), que lê o conteúdo completo do arquivo e o retorna como um string.

    Na linha abaixo, estamos lendo todo o conteúdo do arquivo linguagens.txt e imprimindo no terminal
    """
    print(arquivo.read())

    """
    É sempre importante fechar um arquivo depois de abrí-lo, sob o risco de termos comportamentos inesperados no nosso sistema operacional. Então sempre chamamos o método close() de um arquivo depois que terminamos o seu processamento.
    """
    arquivo.close()
    print('-'*50)

    """
    Caso não queiramos fechar um arquivo automaticamente após processá-lo, podemos abrí-lo utilizando o gerenciador de contexto with, da seguinte maneira:
    """
    # arquivo = open(caminho_arquivo)
    with open(caminho_arquivo) as arquivo:

        """
        O método read() aceita o parâmetro size, que indica a quantidade de bytes que iremos ler do arquivo. No caso de um arquivo texto, é a quantidade de caractes lidos
        """
        print(arquivo.read(10))

        """
        O método readline() lê todos os caractes da linha atual, ou seja, caso seja encontrado o caractere especial de nova linha, ele apenas joga o cursor para a próxima linha.

        Na linha abaixo, apenas de passarmos o valor 100, ele vai ler todos os caractes apenas da linha atual.
        """
        print(arquivo.readline(100))

        """
        Aqui lemos 6 caracteres da linha atual, ou todos os caracteres antes do caractere especial de nova linha
        """
        print(arquivo.readline(6))
        
        """
        O método tell() retorna a posição atual do cursor dentro do arquivo.
        """
        print(f"Posição atual do cursor no arquivo: {arquivo.tell()}")

        """
        O método readlines lê as linhas do arquivo e as retorna como itens de uma lista. Podemos indicar a quantidade de caracteres que será lida. Mesmo se o cursor não parar no final da linha, a linha inteira será retornada
        """
        print(arquivo.readlines(15))


        """
        Lê o resto do conteúdo do arquivo
        """
        print(arquivo.readlines())

        print(f"Posição atual do cursor no arquivo: {arquivo.tell()}")

        """
        Como o cursor está no final do arquivo, qualquer tentativa de ler o seu conteúdo resultará em um retorno de uma string vazia.
        """
        print(arquivo.read(10))

        """
        Se quisermos ler novamente o arquivos, precisamos "rebobinar" o cursor até o início. Para isso, utilizamos o método seek()

        Na linha abaixo, estamos instruindo o cursor a ser movido para o início do arquivo (posição/byte 0)
        """
        arquivo.seek(0)

        print(arquivo.read())