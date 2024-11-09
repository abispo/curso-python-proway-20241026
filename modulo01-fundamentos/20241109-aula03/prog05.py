"""
Funções (Procedures)

Funções recursivas

Uma  função recursiva basicamente é uma função que chama a si mesma. Devido a sua natureza, devemos ter cuidado ao implementar uma função desse tipo, garantindo que haverá um ponto de saída, pois uma função que chama a si mesma indefinidamente, irá causar algum tipo de estouro de memória.

Exemplo: Implementação da função fatorial

5! = 5 * 4 * 3 * 2 * 1  -> 120
"""

def fatorial_nao_recursivo(numero: int) -> int:
    contador = numero
    total = numero

    while contador > 1:
        total = total * (contador - 1)
        # contador = contador - 1
        contador -= 1   # sintaxe curta

    return total


def fatorial_recursivo(numero: int) -> int:
    if numero == 1:
        return numero
    
    return numero * fatorial_recursivo(numero - 1)

if __name__ == "__main__":
    print(f"Fatorial de 5 (não recursivo): {fatorial_nao_recursivo(5)}")
    print(f"Fatorial de 5 (recursivo): {fatorial_recursivo(5)}")