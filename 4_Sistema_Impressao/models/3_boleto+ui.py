class Boleto:
    def __init__(self, codigo: str, valor: float):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self) -> None:
        print(f"boleto - codigo: {self.codigo}, valor R${self.valor}")  # [UI]
