
if __name__ == "__main__":

    valor = input("Informe o seu nível de acesso: ")

    match valor.upper():
        case "USER":
            print("Seu nível de acesso é básico.")

        case "MANAGER":
            print("Seu nível de acesso é intermediário.")

        case "ADMIN":
            print("Seu nível de acesso é avançado.")

        # Opção escolhida quando nenhuma das outras anteriores é verdadeira
        case _:
            print(f"Opção '{valor}' inválida.")
