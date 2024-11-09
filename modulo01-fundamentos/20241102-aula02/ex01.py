"""
Escreva um programa que receba um número maior do que 1 pelo terminal. Em seguida, o programa retorna a soma de 1 até esse número. Ex:

Informe o número: 5
A soma de 1 até 5 é 15

"""

import sys

if __name__ == "__main__":

    numero_informado: int = int(input("Informe um número maior do que 1: "))

    if numero_informado <= 1:
        print("O número informado deve ser maior do que 1.")
        sys.exit(0)

    soma = 0

    for numero in range(1, numero_informado + 1):
        soma += numero

    print(f"A soma dos números entre 1 e {numero} é {soma}.")
