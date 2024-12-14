"""
Programação Orientada a Objetos com Python

Classes, objetos, atributos e métodos
"""

# Utilizamos a palavra reservada 'class' para criar uma classe em Python. De preferência, utilizamos o estilo PascalCase para nomear as classes (ex: Nome, NomeComposto)
class Pokemon:

    # O método __init__ é o método inicializador da classe, ou seja, nesse método podemos colocar os atributos que serão inicializados, chamar métodos, etc.
    # No caso abaixo, estamos definindo o método __init__, que é um método de instância. Nesses casos, obrigatoriamente precisamos passar como primeiro parâmetro o self, que é a referência ao objeto atualmente instanciado
    def __init__(self, name: str, pokemon_type: str, health: int) -> None:

        # Abaixo estamos inicializando 3 atributos: _name, _pokemon_type e _health. Colocamos o underline na frente pra indicar que esses atributos devem ser tratados como atributos privados, já que no Python não temos palavras reservadas para indicar o nível de acesso de um atributo/método.
        self._name = name
        self._pokemon_type = pokemon_type
        self._health = health

    def attack(self):
        # Reforçando, todos os métodos de instância devem começar com o parâmetro self, mesmo que ele não seja utilizado. Abaixo, o objeto está acessando o seu próprio atributo chamado _name
        print(f"{self._name} ataca!")

    def dodge(self):
        print(f"{self._name} desvia!")

    def evolve(self):
        print(f"{self._name} evolui!")

if __name__ == "__main__":
    # Nas linhas abaixo estamos instânciando 2 objetos do tipo Pokemon. Os objetos estão sendo inicializados com os parâmetros. Vale reforçar que são objetos diferentes.
    pikachu = Pokemon(name="Pikachu", pokemon_type="Elétrico", health=60)
    charmander = Pokemon(name="Charmander", pokemon_type="Fogo", health=50)

    pikachu.attack()
    charmander.dodge()