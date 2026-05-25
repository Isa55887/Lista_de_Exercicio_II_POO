class RelatorioSimples:
    def __init__(self, titulo: str):
        self.titulo = titulo

    def imprimir(self) -> None:
        print(f"relatorio: {self.titulo}")  # [UI]
