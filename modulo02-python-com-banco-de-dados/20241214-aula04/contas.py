# Módulo de contas

class ContaFinanceira:

    def __init__(self, nome: str, saldo: float = 0) -> None:
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    @property
    def saldo(self) -> float:
        return self._saldo
    
    def sacar(self, valor: float) -> float:
        if valor > self._saldo:
            # Caso a condição acima seja verdadeira, será lançada uma exceção no nosso código, e o programa irá encerrar imediatamente com uma mensagem de erro.
            raise Exception(
                f"O valor solicitado de R${valor} é maior que o saldo restante na conta R${self._saldo}."
            )
        # self._saldo = self._saldo - valor
        self._saldo -= valor

        return valor
    
    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise Exception(f"O valor a depositar deve ser maior que 0.")
        
        self._saldo += valor

# Abaixo criamos a classe ContaCorrente que irá herdar todos os atributos/métodos da classe ContaFinanceira
class ContaCorrente(ContaFinanceira):
    pass


class ContaInvestimento(ContaFinanceira):

    def __init__(self, nome: str, taxa: float, saldo: float = 0) -> None:
        self._taxa = taxa
        super().__init__(nome, saldo)

    def render(self) -> float:
        rendimento: float = (self._saldo * (self._taxa / 100))
        self._saldo += rendimento

        return rendimento
