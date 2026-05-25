class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_funcionarios = []   # [REPOSITÓRIO]: Armazenamento local

    def adicionar_funcionario(self, funcionario):   # [SERVICES / REPOSITÓRIO]: Lógica para salvar os dados na lista
        self.lista_de_funcionarios.append(funcionario)

    def listar_funcionarios(self):   # [SERVICES + UI]: Comanda a busca e usa comandos de saída para o usuário
        print(f"\n--- lista de funcionarios {self.nome}")
        for f in self.lista_de_funcionarios:
            f.mostrar_dados()

    def mostrar_folha_de_pagamento(self):     # [SERVICES + UI]: Calcula a soma total e imprime o relatório formatado
        print(f"\n--- folha de pagamento: {self.nome} ---")
        total_folha = 0     # Lógica de negócio do Service (acumular valores)
        for f in self.lista_de_funcionarios:
            pagamento = f.calcular_pagamento()
            print(f"funcionario: {f.nome}, salario; R$ {pagamento:.2f}")
            total_folha += pagamento
        print(f"total geral:R$ {total_folha:.2f}")
