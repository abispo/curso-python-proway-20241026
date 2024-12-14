"""
Programação Orientada a Objetos

Polimorfismo
----------

Polimorfismo significa "muitas formas", ou seja, uma função ou método pode ser chamado de diferentes maneiras, trazendo diferentes comportamentos
"""

class Funcionario:

    def __init__(self, nome: str) -> None:
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    def calcular(self):
        # Aqui, todas as classes que herdarem dessa, são obrigadas a implementar esse método
        raise NotImplementedError
    

class FuncionarioCLT(Funcionario):

    def __init__(self, nome: str, salario: float) -> None:
        self._salario = salario
        super().__init__(nome)

    def calcular(self) -> float:
        return self._salario
    

class FuncionarioTerceirizado(Funcionario):
    
    def __init__(self, nome: str, qtd_horas_trabalhadas: int, valor_hora: float) -> None:
        self._qtd_hotas_trabalhadas = qtd_horas_trabalhadas
        self._valor_hora = valor_hora
        super().__init__(nome)

    def calcular(self) -> float:
        return self._qtd_hotas_trabalhadas * self._valor_hora
    

class FuncionarioComissionado(Funcionario):

    def __init__(self, nome: str, valor_total_vendido: float, comissao: float) -> None:
        self._valor_total_vendido = valor_total_vendido
        self._comissao = comissao
        super().__init__(nome)

    def calcular(self) -> float:
        return self._valor_total_vendido * (self._comissao / 100)
    

class FolhaDePagamento:
    def __init__(self, funcionarios):
        self._funcionarios = funcionarios

    def gerar(self):
        print("=== GERAÇÃO DE FOLHA DE PAGAMENTO ===")
        for funcionario in self._funcionarios:
            nome_funcionario = funcionario.nome
            tipo_funcionario = funcionario.__class__.__name__
            salario_funcionario = funcionario.calcular()

            print("= Dados do Funcionário")
            print(f"= Nome: {nome_funcionario}")
            print(f"= Tipo: {tipo_funcionario}")
            print(f"= Salário: {salario_funcionario}")
            print("="*30)

if __name__ == "__main__":
    maria = FuncionarioCLT(nome="Maria", salario=1970)
    jose = FuncionarioTerceirizado(nome="José", qtd_horas_trabalhadas=42, valor_hora=30)
    jessica = FuncionarioComissionado(nome="Jéssica", valor_total_vendido=104673.12, comissao=3)

    folha_de_pagamento = FolhaDePagamento([maria, jose, jessica])
    folha_de_pagamento.gerar()