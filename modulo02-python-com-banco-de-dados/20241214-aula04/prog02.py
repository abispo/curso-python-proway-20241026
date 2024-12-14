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
