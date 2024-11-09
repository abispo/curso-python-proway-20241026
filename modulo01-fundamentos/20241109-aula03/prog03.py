"""
Funções (Procedures)

É possível também definir parâmetros opcionais em uma função python, ou seja, parâmetros que não necessariamente precisam receber um valor. Para isso, devemos definir um valor padrão para esses parâmetros.
"""

def calculo_hora_extra(valor_hora: float, qtd_horas_extras: int = 0):
    return valor_hora * qtd_horas_extras


if __name__ == "__main__":

    # Passamos todos os parâmetros de maneira posicional
    print(f"{calculo_hora_extra(23.5, 2):.2f}")

    # Passamos todos os parâmetros por nome
    print(f"{calculo_hora_extra(qtd_horas_extras=4, valor_hora=10):.2f}")

    # Passamos todos os parâmetros, e indicamos apenas o nome do qtd_horas_extras
    print(f"{calculo_hora_extra(33.5, qtd_horas_extras=3):.2f}")

    # Não passamos o valor do parâmetro qtd_horas_extras, portanto foi assumido o valor padrão
    print(f"{calculo_hora_extra(27.5):.2f}")
    
    # Você sempre deve passar os parâmetros por posição antes dos parâmetros por nome. A linha abaixo causa um erro de sintaxe, pois temos um parâmetro posicional (obrigatório) após um parâmetro nomeado (que pode ser opcional)
    # print(f"{calculo_hora_extra(qtd_horas_extras=3, 44):.2f}")