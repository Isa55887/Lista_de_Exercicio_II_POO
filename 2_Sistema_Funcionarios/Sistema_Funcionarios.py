from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"nome: {self.nome}, cpf: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self):
        pass

class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome, cpf, salario_mensal):
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self):
        return self.salario_mensal
    
class FuncionarioHosrista(Funcionario):
    def __init__(self, nome, cpf, horas_trabalhadas, valor_hora):
        super().__init__(nome, cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        return self.horas_trabalhadas * self.valor_hora
    
class FuncionarioComissado(Funcionario):
    def __init__(self, nome, cpf, total_vendas, percentual_comissao):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao
        
    def calcular_pagamento(self):
        return self.total_vendas * (self.percentual_comissao / 100)
    
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.lista_de_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\n--- lista de funcionarios {self.nome}")
        for f in self.lista_de_funcionarios:
            f.mostrar_dados()

    def mostrar_folha_de_pagamento(self):
        print(f"\n--- folha de pagamento: {self.nome} ---")
        total_folha = 0
        for f in self.lista_de_funcionarios:
            pagamento = f.calcular_pagamento()
            print(f"funcionario: {f.nome}, salario; R$ {pagamento:.2f}")
            total_folha += pagamento
        print(f"total geral:R$ {total_folha:.2f}")
