"""
Escreva um programa em Python que inverta uma lista de números. Exemplo:
lista = [4, 7, 8, 1, 9]
lista_invertida = [9, 1, 8, 7, 4]

"""

if __name__ == "__main__":

    # Maneira 1
    lista = [4, 7, 8, 1, 9]
    lista_final = []

    for numero in lista:
        # Aqui inserimos o item sempre no início da lista. Assim, os próximos itens vão "empurrando" para a direita os anteriores.
        lista_final.insert(0, numero)

    print(lista)
    print(lista_final)
    print('-'*50)

    # Maneira 2 (Utilizando slice (fatiamento) de lista)
    print(lista[::-1])