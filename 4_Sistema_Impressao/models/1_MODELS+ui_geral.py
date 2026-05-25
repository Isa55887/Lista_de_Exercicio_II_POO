class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...

class Boleto:
    def __init__(self, codigo: str, valor: float):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self) -> None:
        print(f"boleto - codigo: {self.codigo}, valor R${self.valor}")

class Etiqueta:
    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        print(f"etiqueta - destinatario: {self.destinatario}, endereco:{self.endereco}")

class RelatorioSimples:
    def __init__(self, titulo: str):
        self.titulo = titulo

    def imprimir(self) -> None:
        print(f"relatorio: {self.titulo}")
