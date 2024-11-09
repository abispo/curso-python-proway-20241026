"""
Funções (Procedures)

Também podemos passar valores por meio de parâmetros. Esses valores serão acessíveis dentro das funções.
"""

# É possível especificar o tipo de valor que os parâmetros devem receber. Como Python é uma linguagem dinamicamente tipada, mesmo que outro tipo de valor seja recebido, não haverá problema.
# Também é possível especificar o tipo de retorno de uma função/método. No caso abaixo, estamos indicando que a função calculo_imc vai retornar um valor do tipo float
def calculo_imc(altura: float, peso: float) -> float:
    return peso / (altura * altura)

if __name__ == "__main__":
    print(f"IMC: {calculo_imc(1.81, 89.5):.1f}")

    # Quando chamamos uma função, podemos informar os valores dos parâmetros de 2 maneiras: De maneira posicional ou pelo nome do parâmetro. Acima, passamos os valores de maneira posicional, ou seja, devemos passar esses valores respeitando a ordem dos parâmetros

    # Podemos passar os valores indicando explicitamente pra qual parâmetro cada valor vai, da seguinte maneira:
    print(f"IMC: {calculo_imc(peso=91, altura=1.74):.1f}.")

    # Vale notar, que dessa maneira não importa a ordem dos valores passados

    # Agora imagine um cenário onde você tem vários valores que precisam ser passados para uma função. Por exemplo, uma lista de tuplas, em que cada tupla armazena a altura e o peso que será feito o cálculo de IMC

    lista_medidas = [
        (1.99, 132.5), (1.73, 58.9), (1.80, 69.4), (2.01, 99.4), (1.93, 116.4)
    ]

    # Maneira 'intuitiva' se fazer o cálculo de todos os valores da lista
    for medidas in lista_medidas:
        altura = medidas[0]
        peso = medidas[1]

        print("Peso: {}, Altura: {}, IMC: {:.1f}".format(
            peso, altura, calculo_imc(altura, peso)
        ))
    print('-'*50)

    # Utilizando desempacotamento de valores de uma lista
    for medidas in lista_medidas:
        altura = medidas[0]
        peso = medidas[1]
    
        print("Peso: {}, Altura: {}, IMC: {:.1f}".format(
            peso, altura, calculo_imc(*medidas)
        ))

    """
    No último for, estamos desempacotandos os valores da lista na funçao calculo_imc. Basicamente, passamos a lista de valores por posição para a função. Por exemplo: Se o item que está sendo processado, é a tupla (1.80, 89.4), a função vai ser chamada passando esses valores de maneira posicional, ou seja, calculo_imc(1.80, 89.4).

    Quando estamos trabalhando com listas ou tuplas, obrigatoriamente precisamos utilizar apenas 1 asterisco, que irá passar os valores de maneira posicional
    """
    print('='*50)

    # Agora, vamos imaginar um cenário onde temos uma lista de dicionários com informações sobre o peso/altura

    lista_pacientes = [
        {"peso": 121.5, "altura": 1.78},
        {"peso": 88.1, "altura": 1.74},
        {"peso": 100.3, "altura": 1.89},
        {"peso": 79.9, "altura": 1.68},
        {"peso": 94.5, "altura": 1.75},
    ]

    # Calculando o imc de maneira 'intuitiva'
    for paciente in lista_pacientes:
        print("Peso: {}, Altura: {}, IMC: {:.1f}".format(
            paciente.get("peso"),
            paciente.get("altura"),
            calculo_imc(paciente.get("altura"), paciente.get("peso"))
        ))
    print('-'*50)

    # Calculando o imc utizando o desempacotamento dos valores de um dicionário
    for paciente in lista_pacientes:
        print("Peso: {}, Altura: {}, IMC: {:.1f}".format(
            paciente.get("peso"),
            paciente.get("altura"),
            calculo_imc(**paciente)
        ))

        # * calculo_imc(1.65, 78.1)
        # ** calculo_imc(peso=32, altura=324)
    