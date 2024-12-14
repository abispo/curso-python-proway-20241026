"""
Programação Orientada a Objetos

Composição
----------

Composição ocorre quando uma classe compõe ou é composta por outra/outras classes
"""

from random import shuffle

class Carta:

    def __init__(self, naipe: str, valor: str) -> None:
        self._naipe = naipe
        self._valor = valor

    # Método utilizado para definir a representação em string desse objeto
    def __str__(self):
        return f"{self._valor}{self._naipe}"
    
    # Mesma coisa do __str__, porém é útil quando o objeto está em um container (lista, dicionario, etc)
    def __repr__(self):
        return f"{self._valor}{self._naipe}"


class Baralho(object):

    def __init__(self):
        # Atributo que irá controlar as cartas que compõem o baralho
        self._cartas = []

        # Lista de valores que será utilizada para inicializar esse baralho
        self._valores = [
            '2', '3', '4', '5',
            '6', '7', '8', '9',
            '10', 'J', 'Q', 'K',
            'A'
        ]

        # Lista de naipes que será utilizada para inicializar esse baralho
        self._naipes = [
            '\u2660', '\u2665', '\u2663', '\u2666'
        ]

        # Abaixo será preenchida a lista de cartas desse baralho. Para cada naipe, vamos iterar sobre a lista de valores. Dentro do bloco mais interno, instanciamos a classe Carta passando os valores de naipe e valor, e ao mesmo tempo adicionamos esse objeto na lista _cartas
        for naipe in self._naipes:
            for valor in self._valores:
                self._cartas.append(
                    Carta(naipe=naipe, valor=valor)
                )

        shuffle(self._cartas)

    def __str__(self):
        # O método join concatena uma lista de valores em uma string, separada pelo(s) caractere(s) informados na string
        return ", ".join(str(carta) for carta in self._cartas)

if __name__ == "__main__":
    baralho = Baralho()
    print(baralho)
