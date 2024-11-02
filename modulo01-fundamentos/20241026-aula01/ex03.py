# Escreva um programa que leia três números inteiros e exiba o maior e o menor deles.

if __name__ == "__main__":
    
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    numero3 = int(input("Informe o terceiro número: "))

    maior = max(numero1, numero2, numero3)
    menor = min(numero1, numero2, numero3)

    print(f"O número {maior} é o maior número.")
    print(f"O número {menor} é o menor número.")