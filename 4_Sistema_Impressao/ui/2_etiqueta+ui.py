class Etiqueta:
    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        print(f"etiqueta - destinatario: {self.destinatario}, endereco:{self.endereco}")  # [UI]
