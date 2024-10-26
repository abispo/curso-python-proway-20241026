# Isso é um comentário em Python. Comentários em Python iniciam com o caractere '#'.
# Comentários não são executados pelo interpretador da linguagem, ou seja, podemos digitar qualquer coisa.

"""
Python não possui um caractere especial para comentários multilinha, para isso podemos utilizar a sintaxe de strings multilinha, que sempre começam e terminam com 3 aspas (tanto simples (') quanto duplas ("))
"""

"""
Assim como a maioria das linguagens, o Python possui estruturas de controle de condição, ou seja, estruturas que verificam se um determinado valor é verdadeiro ou falso.

No Python, temos a estrutura if... elif... else, e também a estrutura match case.

No caso abaixo, estamos verificando se o valor da variável __name__ é igual a string "__main__". A váriável __name__ é criada automaticamente quando o interpretador Python é chamado. O valor __main__ vem do fato de que o arquivo está sendo chamado diretamente pelo interpretador, e não importado via outro módulo
"""
if __name__ == "__main__":
    """
    Sempre que usamos uma estrutura de controle de condição ou repetição, estamos criando um novo bloco de código. Aqui devemos tomar cuidado, pois sempre que criamos um novo bloco de código, precisamos começar esse bloco com o espaçamento correto. Por padrão, o Python indica utilizar um espaçamento de tamanho 4
    """
    nome = input("Informe o seu nome: ")

    """
    Acima, estamos utilizando a função built-in input(). Funções built-in são funções carregadas automaticamente pelo interpretador Python (https://www.w3schools.com/python/python_ref_functions.asp). No caso da função input(), ela espera que o usuário digite algo pelo terminal, e retorna como string.

    string é um dos tipos de dados do Python. Strings são basicamente textos. Python possui outros tipos de dados, como:
        * Numéricos (int, float, complex)
        * Booleanos (True, False)
        * Listas
        * Dicionários
        * e outros

    nome é a variável que está recebendo o retorno da função input(). Variáveis no Python são dinamicamente tipadas, ou seja, é o próprio interpretador que descobre o tipo de dado da variável. No caso acima, estamos salvando na variável nome o que o usuário digitou pelo terminal. O caractere '=' é o operador de atribuição, ou seja, estamos atribuindo a variável nome o valor retornado da função input()
    """
    
    print(f"Olá {nome}. Bem-vindo(a) ao curso de Python.")          # Sintaxe f-strings
    print("Olá " + nome + ". Bem-vindo(a) ao curso de Python.")     # Sintaxe "comum"
    print("Olá %s. Bem-vindo(a) ao curso de Python" % (nome,))      # Sintaxe Python 2.*
    print("Olá {}. Bem-vindo(a) ao curso de Python. {}".format(nome, 10))
    print("Olá {nome}. Bem-vindo(a) ao curso de Python.".format(
        nome=nome
    ))

    """
    A função built-in print() imprime um valor no terminal. Acima estamos utilizando o sintaxe de f-strings para concatenar o valor da variável nome com o restante do texto.
    """