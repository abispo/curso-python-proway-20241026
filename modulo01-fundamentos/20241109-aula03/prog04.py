"""
Funções (procedures)

Também é possível criar funções que recebem uma quantidade arbitrária de parâmetros, ou seja, uma função que pode receber quantos parâmetros quisermos
"""

# Função que calcula a média de nível de um gás em um período de medição. Por padrão, o *args é entendido pelo Python como uma tupla
def calculo_media_gas(*args) -> float:
    return sum(args) / len(args)

if __name__ == "__main__":
    calculo_media_1 = calculo_media_gas(0.6, 0.4, 0.1, 0.2, 0.1, 0.3)
    print(f"Média de cálculo dos níveis de gás: {calculo_media_1:.1f}")

    calculo_media_1 = calculo_media_gas(0.1, 0.1, 0.3)
    print(f"Média de cálculo dos níveis de gás: {calculo_media_1:.1f}")