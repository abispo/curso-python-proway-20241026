# Crie um programa que peça ao usuário para digitar dois números inteiros e exiba a soma, subtração, multiplicação e divisão dos números.

if __name__ == "__main__":

    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))

    # Em uma f-string, além de ser possível colocar qualquer valor (numero, string, variável, etc) dentro das chaves, podemos colocar também qualquer expressão python válida

    mensagem = f"""
    {numero1} + {numero2} é igual a {numero1 + numero2}
    {numero1} - {numero2} é igual a {numero1 - numero2}
    {numero1} * {numero2} é igual a {numero1 * numero2}
    {numero1} / {numero2} é igual a {numero1 / numero2}

"""
    
    print(mensagem)

    # print(f"{numero1} + {numero2} é igual a {numero1 + numero2}")
    # print(f"{numero1} - {numero2} é igual a {numero1 - numero2}")
    # print(f"{numero1} * {numero2} é igual a {numero1 * numero2}")
    # print(f"{numero1} / {numero2} é igual a {numero1 / numero2}")