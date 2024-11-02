"""
Escreva um programa que leia o salário de um funcionário e exiba o valor do salário líquido, descontando o INSS. As faixas de desconto são as seguintes:

Até R$ 1.320,00 7,5%
De R$ 1.320,01 a R$ 2.571,29 9%
De R$ 2.571,30 até R$ 3.856,94 12%
Acima de R$ 3.856,95 14%

"""

if __name__ == "__main__":
    
    PRIMEIRA_FAIXA  = 7.5 / 100
    SEGUNDA_FAIXA   = 9 / 100
    TERCEIRA_FAIXA  = 12 / 100
    QUARTA_FAIXA    = 14 / 100

    salario_bruto = float(input("Informe o seu salário: "))
    salario_liquido = 0
    desconto = 0

    if salario_bruto < 1320:
        salario_liquido = salario_bruto - (salario_bruto * PRIMEIRA_FAIXA)
        desconto = PRIMEIRA_FAIXA * 100

    elif salario_bruto >= 1320 and salario_bruto < 2751.30:
        salario_liquido = salario_bruto - (salario_bruto * SEGUNDA_FAIXA)
        desconto = SEGUNDA_FAIXA * 100

    elif salario_bruto >= 2751.30 and salario_bruto < 3856.95:
        salario_liquido = salario_bruto - (salario_bruto * TERCEIRA_FAIXA)
        desconto = TERCEIRA_FAIXA * 100

    else:
        salario_liquido = salario_bruto - (salario_bruto * QUARTA_FAIXA)
        desconto = QUARTA_FAIXA * 100

    print(f"Seu salário bruto foi de R$ {salario_bruto}.")
    print(f"O desconto aplicado foi de {desconto:.1f}%.")
    print(f"Seu salário líquido é de R$ {salario_liquido:.2f}.")