"""
Funções (procedures)

Também é possível criar funções que recebem uma quantidade arbitrária de parâmetros, ou seja, uma função que pode receber quantos parâmetros quisermos. Podemos chamar isso de empacotamento de parâmetros
"""

# Função que calcula a média de nível de um gás em um período de medição. Por padrão, o *args é entendido pelo Python como uma tupla
def calculo_media_gas(*args) -> float:
    return sum(args) / len(args)

# Função que recebe um dicionário e imprime as chaves e os valores
def mostra_info_usuario(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

    print('-'*50)

if __name__ == "__main__":
    calculo_media_1 = calculo_media_gas(0.6, 0.4, 0.1, 0.2, 0.1, 0.3)
    print(f"Média de cálculo dos níveis de gás: {calculo_media_1:.1f}")

    # É importante lembrar que o parâmetro *args vai receber todos os valores passados de maneira posicional
    calculo_media_1 = calculo_media_gas(0.1, 0.1, 0.3)
    print(f"Média de cálculo dos níveis de gás: {calculo_media_1:.1f}")
    
    usuario1 = {"nome": "Barbara", "cep": "89023453", "setor": 10}
    usuario2 = {"nome": "João", "idade": 20}

    mostra_info_usuario(nome="José", idade=50)
    mostra_info_usuario(nome="Maria", idade=40, estado="SC", genero="Feminino")
    mostra_info_usuario(nome="Marcos")
    mostra_info_usuario(**usuario1)
    mostra_info_usuario(**usuario2)