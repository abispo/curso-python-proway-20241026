"""
Laços de repetição

O laço for geralmente é utilizado quando queremos percorrer(iterar) uma estrutura de dados do tipo sequência. Ou seja, utilizamos quando queremos acessar sequencialmente os dados.

"""

# Importamos a função randint do módulo random. Essa função gera um número aleatório entre um intervado de números
from random import randint

if __name__ == "__main__":

    # Abaixo estamos criando uma lista. Lista é um dos tipos de dados em Python, ela consegue armazenar qualquer tipo de valor, inclusive outras listas.
    # Podemos criar uma lista utilizando a função built-in list() ou utilizando a sintaxe simples ([])
    lista_numeros = []
    bonus = 0
    soma = 0

    # A função range() gerá uma sequência de números. Por padrão, começando por 0 e gerando a quantidade de números informada
    for _ in range(5): 
        # O método append de uma lista adiciona um novo item no final da lista. Na linha abaixo, estamos adicionando na lista o número aleatório gerado pela função randint
        lista_numeros.append(randint(1, 100))

    for numero in lista_numeros:
        
        if numero < 10:
            print("Você tirou um número muito baixo. Finalizando.")
            # Caso o comando break seja executado dentro do laço for, o laço finaliza imediatamente, independentemente da quantidade de itens a serem lidos na sequência.
            break

        elif numero >= 90:
            print("Você tirou um número bem alto!")
            bonus += 200
            # Caso o comando continue seja executado dentro do laço for, ele ignora as instruções seguintes se existitem, e volta ao início do laço, processando o próximo item
            continue
        
        else:
            soma += numero

    # O bloco de código else de um laço for, somente será executado caso nenhuma instrução break tenha sido executada dentro do laço.
    else:
        print("Nenhum número abaixo de 10 gerado.")

    # soma = soma + bonus
    soma += bonus

    print(f"Valor final: {soma}.")