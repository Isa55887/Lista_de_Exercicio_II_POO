class Midia(ABC):
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Duração: {self.duracao} min"
    
    @abstractmethod
    def reproduzir(self):
        pass
