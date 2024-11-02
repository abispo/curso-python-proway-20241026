"""
Laços de repetição

Laço while

O laço while é utilizando quando queremos executar um bloco e código repetidas vezes, enquanto uma determinada condição é verdadeira
"""

from random import randint
from time import sleep

if __name__ == "__main__":

    """
    Dicionário é um outro tipo de dado em Python, caracterizado pelo formato chave: valor. Como valor, podemos ter qualquer tipo de dados em Python (strings, numeros, listas, outros dicionarios, etc). Como chave, podemos ter apenas dados dos tipos básicos de python (string, numero e booleano)
    """
    heroi = {
        "nome": "Aragorn",
        "ataque": 15,
        "defesa": 10,
        "hp": 20
    }

    monstro = {
        "nome": "Orc",
        "ataque": 11,
        "defesa": 12,
        "hp": 16
    }

    vencedor = None

    while not vencedor:

        for numero in range(2, 4):
            if numero % 2 == 0:
                atacante = heroi
                defensor = monstro

            else:
                atacante = monstro
                defensor = heroi
            
            print(f"{atacante['nome']} ataca {defensor['nome']}.")
            dado_ataque = randint(1, 12)
            dado_defesa = randint(1, 12)

            ataque_atacante = atacante.get("ataque") + dado_ataque
            defesa_defensor = defensor.get("defesa") + dado_defesa

            sleep(1)

            if ataque_atacante > defesa_defensor:
                print(f"{atacante['nome']} acertou um golpe no {defensor['nome']}!")
                defensor["hp"] = defensor["hp"] - (ataque_atacante - defensor["defesa"])

            else:
                print(f"{defensor['nome']} defendeu o ataque de {atacante['nome']}!")

            sleep(1)

            if defensor["hp"] <= 0:
                vencedor = atacante
                break


    print(f"Vencedor: {vencedor}.")