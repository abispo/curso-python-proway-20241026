"""
Escreva um programa que gere números randômicos de 0 até 50. Salve esse números em uma lista. Em seguida, informe quais são o maior e o menor número dessa lista. Dica: Utilize as funções built-in max() e min()

"""

from random import randint

if __name__ == "__main__":

    lista_randomicos = [randint(0, 50) for _ in range(20)]
    
    print(f"Lista números: {lista_randomicos}")
    print(f"Maior número: {max(lista_randomicos)}")
    print(f"Menor número: {min(lista_randomicos)}")