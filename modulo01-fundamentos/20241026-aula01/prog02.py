
if __name__ == "__main__":

    # Como a função built-in input() retorna apenas strings, para ser possível fazer o cálculo de IMC, precisamos convertes essas strings em tipos numéricos. Abaixo estamos utilizando a função float() para converter uma string em um número com casa decimal. Esse é o conhecido cast de valores. Os possíveis valores numéricos são int() e complex()

    peso = float(input("Informe o seu peso em kg (ex: 78.5): "))
    altura = float(input("Informe a sua altura em metros (ex: 1.81): "))

    """
    Abaixo estamos usando os operadores aritméticos divisão (/) e exponenciação (**). Temos a seguinte lista de operadores aritméticos em Python:

        +   Adição
        -   Subtração
        *   Multiplicação
        /   Divisão
        %   Resto da Divisão
        **  Exponenciação
        //  Produto da divisão

        """

    imc = peso / (altura ** 2)

    """
    Abaixo utilizamos a estrutura de controle de repetição if... elif... else. O if e o elif recebem uma expressão válida em Python que deve retornar um valor booleano. Se esse valor for True, o bloco de código é executado.

    Caso nenhuma das comparações de if e elif retornem um valor verdadeiro, se houver, será executado o bloco de código do else.
    
    A linha abaixo utiliza o operador menor que (<) para verificar se o valor calculado do IMC é menor do que 18.5. Se sim, ele irá executar o bloco de código do if, se não, ele irá para a próxima comparação
    """
    if imc < 18.5:
        mensagem = "Você está abaixo do peso."

        """
        No Python, temos os seguintes operadores de comparação:
            >   Maior que
            >=  Maior ou igual a
            <   Menor que
            <=  Menor ou igual a
            ==  Igual
            !=  Diferente
        """

    elif imc >= 18.5 and imc <= 24.9:
        """
        Além dos operadores de comparação, também temos os operadores lógicos, que vão comparar o valor verdadeiro de 2 expressões. Temos os seguintes operadores lógicos:

        and     ->  E
        or      ->  OU
        not     ->  NÃO (Negação lógica)
        """
        mensagem = "Você está com o peso normal."

    elif imc >= 25 and imc <= 29.9:
        mensagem = "Você está com sobrepeso."

    elif imc >= 30 and imc <= 34.9:
        mensagem = "Você está com obesidade grau I."

    elif imc >= 35 and imc <= 39.9:
        mensagem = "Você está com obesidade grau II."

    else:
       mensagem = "Você está com obesidade grau III."

    print(f"Seu IMC é de {imc:.2f}. {mensagem}")
