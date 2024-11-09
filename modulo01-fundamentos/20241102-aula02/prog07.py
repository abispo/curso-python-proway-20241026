"""
Escreva um programa que receba nome, idade e sexo de 3 usuários. Em seguida, mostre quantos usuários são do sexo masculino, quantos são do sexo feminino e qual é a média de idade. Exemplo:
Nome: João
Idade: 32
Sexo: M

Nome: Maria
Idade: 17
Sexo: F

Nome: Vanessa
Idade: 28
Sexo: F

Quantidade de usuários do sexo masculino: 1
Quantidade de usuários do sexo feminino: 2
Média de idade: 25.67

"""

if __name__ == "__main__":

    lista_usuarios = []

    for _ in range(3):
        
        nome = input("Informe o nome do usuário: ")
        idade = int(input("Informe a idade do usuário: "))
        sexo = input("Informe o sexo do usuário: ")

        print('-'*50)

        lista_usuarios.append({
            "nome": nome,
            "idade": idade,
            "sexo": sexo
        })

    qtd_sexo_masculino = len([usuario for usuario in lista_usuarios if usuario.get("sexo") == "M"])
    qtd_sexo_feminino = len([usuario for usuario in lista_usuarios if usuario.get("sexo") == "F"])
    media_idade = sum([usuario.get("idade") for usuario in lista_usuarios]) / len(lista_usuarios)

    print(f"Quantidade de usuários do sexo masculino: {qtd_sexo_masculino}")
    print(f"Quantidade de usuários do sexo feminino: {qtd_sexo_feminino}")
    print(f"Média de idade: {media_idade:.1f}")