# Escreva um programa que solicite o nome, a idade e o sexo do usuário. Em seguida, exiba uma mensagem personalizada informando se o usuário é homem ou mulher e se é maior ou menor de idade.

import sys

if __name__ == "__main__":

    nome = input("Informe o seu nome: ")
    idade = int(input("Informe a sua idade: "))
    sexo = input("Informe o seu sexo (M ou F): ")

    if idade < 18:
        maioridade = False

    else:
        maioridade = True

    # Se
    if sexo.upper() == "M":
        genero = "Masculino"

    # Senão se
    elif sexo.upper() == "F":
        genero = "Feminino"

    # Senão
    else:
        print(f"O valor '{sexo}' não é válido (M ou F)")
        sys.exit(0)

    mensagem = f"""
O usuário '{nome}' é do gênero {genero} e é {'maior de idade' if maioridade else 'menor de idade'}.
"""
    
    print(mensagem)