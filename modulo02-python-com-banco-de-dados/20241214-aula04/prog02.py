"""
Programação Orientada a Objetos

Herança
-------

A Herança ocorre quando uma classe filha(ou subclasse) herda atributos e métodos de uma classe mãe (ou superclasse).
"""

from contas import ContaCorrente, ContaInvestimento

if __name__ == "__main__":

    conta_viacredi = ContaCorrente(nome="Conta Viacredi")
    conta_viacredi.depositar(100)
    print(f"Saldo da conta '{conta_viacredi.nome}': {conta_viacredi.saldo}")
    conta_viacredi.sacar(55)
    print(f"Saldo da conta '{conta_viacredi.nome}': {conta_viacredi.saldo}")

    conta_poupanca_caixa = ContaInvestimento(
        "Conta Poupança Caixa",
        1,
        100
    )

    rendimento = conta_poupanca_caixa.render()
    print(f"A conta '{conta_poupanca_caixa.nome}' rendeu R$ {rendimento:.2f}.")
    print(f"O saldo atual da conta '{conta_poupanca_caixa.nome}' é de {conta_poupanca_caixa.saldo}")