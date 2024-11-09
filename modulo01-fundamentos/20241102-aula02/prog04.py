"""
Escreva um programa que converta uma lista de inteiros em apenas 1 inteiro. Exemplo:
lista = [4, 7, 10, 24]
Saída: 471024
"""

from random import randint

if __name__ == "__main__":

    lista_numeros_randomicos = [randint(1, 10) for _ in range(randint(3, 8))]
    print(f"Lista de números: {lista_numeros_randomicos}")

    numero_concatenado = int("".join([str(numero) for numero in lista_numeros_randomicos]))
    print(f"Número concatenado: {numero_concatenado}")