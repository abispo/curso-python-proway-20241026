"""
Entrada e Saída (I/O) de arquivos em Python

Escrita de arquivos .txt
"""

from random import randint

import os

if __name__ == "__main__":
    
    numeros = [
        str(randint(0, 999999)).zfill(6),
        str(randint(0, 999999)).zfill(6),
        str(randint(0, 999999)).zfill(6),
        str(randint(0, 999999)).zfill(6),
        str(randint(0, 999999)).zfill(6),
    ]

    # O método de string zfill() preenche com zeros à esquerda o valor especificado

    caminho_pasta_saida = os.path.join(os.getcwd(), "saida")

    # A função exists do modulo os.path verifica se um arquivo ou pasta existe. Se sim, retorna True
    if not os.path.exists(caminho_pasta_saida):
        # A função mkdir do pacote os cria uma pasta no caminho especificado
        os.mkdir(caminho_pasta_saida)

    # Aqui estamos abrindo o arquivo numeros.txt que está dentro da pasta saida, no modo de escrita. Se o arquivo não existir, será criado.
    arquivo_numeros = os.path.join(caminho_pasta_saida, "numeros.txt")
    with open(arquivo_numeros, "w", encoding="utf-8") as arquivo:
        for numero in numeros:
            arquivo.write(f"{numero}\n")

    with open(arquivo_numeros, mode='a', encoding="utf-8") as arquivo:
        arquivo.writelines([
            "Números da loteria federal\n",
            "Concurso 1111\n",
            "Números gerados aleatoriamente\n",
        ])
