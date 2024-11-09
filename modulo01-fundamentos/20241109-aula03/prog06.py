"""
Funções (Procedures)

Função lambda

Uma função lambda nada mais é do que uma função anônima, ou seja, uma função que não possui nome. Geralmente criamos funções lambda nos casos onde uma determinada função possui um parâmetro que deve ser do tipo função, mas não queremos criar essa função da maneira tradicional
"""

from random import randint
from typing import Dict

def compara(acesso: Dict[str, bool]) -> bool:
    return acesso.get("permitido")

if __name__ == "__main__":
    
    lista_acessos = [
        {"nome": "José", "permitido": bool(randint(0, 1))},
        {"nome": "Maria", "permitido": bool(randint(0, 1))},
        {"nome": "Carlos", "permitido": bool(randint(0, 1))},
        {"nome": "Daniela", "permitido": bool(randint(0, 1))},
        {"nome": "Barbara", "permitido": bool(randint(0, 1))}
    ]

    print(lista_acessos)

    lista_permitidos = list(filter(compara, lista_acessos))

    # A função lambda pode ou não receber parâmetros, separados por vírgula. O corpo da função lambda vem depois dos 2 pontos
    # No caso abaixo, a função lambda está recebendo o parâmetro usuário, que é um item da lista_acessos. Caso essa função retorne True, o dado será retornado no fim da função.
    lista_permitidos = list(filter(lambda usuario: usuario.get("permitido"), lista_acessos))
    print('*'*50)

    print(lista_permitidos)

    # Também podemos utilizar funções lambda na função map
    print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))