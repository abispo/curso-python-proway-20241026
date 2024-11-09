"""
Escreva um programa em Python que gere uma lista randômica de 50 números de 1 até 50. Em seguida, retire os valores repetidos dessa lista (utilize a função randint() do pacote random)
"""

from random import randint

if __name__ == "__main__":
    lista_nao_repetidos = []
    lista_numeros = [randint(1, 50) for _ in range(50)]

    for numero in lista_numeros:
        if numero not in lista_nao_repetidos:
            lista_nao_repetidos.append(numero)

    print(f"Lista original: {lista_numeros}")
    print(f"Lista não repetidos: {sorted(lista_nao_repetidos)}")

    print('-'*50)
    # Utilizando um set
    print(f"Lista não repetidos (set) {list(set(lista_numeros))}")