from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Duração: {self.duracao} min"
    
    @abstractmethod
    def reproduzir(self):
        pass

class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"reproduzindo video: {self.titulo} ({self.resolucao})....")

class Podcast(Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"ouvindo Podcast: {self.titulo} com {self.apresentador}...")

class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"lendo texto narrado: {self.titulo}, ({self.idioma})...")
