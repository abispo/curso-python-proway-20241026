"""
Funções (Procedures)

Funções são blocos de código que executam uma determinada tarefa. Devido a sua natureza, funções podem ser definidas 1 vez, e usadas várias vezes em qualquer lugar do nosso código. Além disso, funções podem receber valores através de parâmetros (ou argumentos), e também podem retornar valores resultantes dessa tarefa realizada.

Em Python, utilizamos a palavra reservada 'def' para criar funções.
"""

# Após a palavra reservada 'def', indicamos o nome da função, que pode ou não ter parâmetros
def ola():
    # Aqui está o corpo da função. Sempre que criamos uma função, criamos um novo bloco de código
    print("Olá.")


if __name__ == "__main__":
    ola()