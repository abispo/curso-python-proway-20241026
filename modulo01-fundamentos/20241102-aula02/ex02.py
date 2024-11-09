"""
Escreva um programa que receba números pelo terminal. Se o usuário digitar o número 0, o programa para de receber números pelo terminal e retorna uma lista dos quadrados desses números. Exemplo:
Digite um número: 4
Digite um número: 2
Digite um número: 6
Digite um número: 0

Lista dos quadrados: [16, 4, 36]
"""

if __name__ == "__main__":

    lista_numeros = []

    while True:
        # O block try...except serve para capturar exceções que eventualmente podem ocorrer no nosso código
        # No caso abaixo, se o usuário informar qualquer caractere diferente de número, será gerada uma exceção do tipo ValueError, que será tratada posteriormente.
        try:
            numero: int = int(input("Informe um número (0 para SAIR): "))

            if numero == 0:
                break

            lista_numeros.append(numero)

        except ValueError:
            print("Você deve informar um número inteiro válido")
            continue

    print(f"Lista original: {lista_numeros}")

    """
    Abaixo utilizamos uma list comprehension para exibir a lista dos quadrados. Por exemplo, a lista abaixo poderia ser criada intuitivamente da seguinte maneira:

    lista_quadrados = []
    for numero in lista_numeros:
        lista_quadrados.append(numero * numero)

    print(lista_quadrados)
    """
    
    print(f"Lista dos quadrados: {[numero * numero for numero in lista_numeros]}")