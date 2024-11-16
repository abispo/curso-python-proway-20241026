import os

if __name__ == "__main__":

    caminho_arquivo = os.path.join(os.getcwd(), "arquivos", "nomes.txt")

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:
            linha = linha.replace('\n', "")
            print(linha)