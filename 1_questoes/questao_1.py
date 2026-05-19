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

class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_midias = []

    def adicionar_midia(self, midia):
        self.lista_de_midias.append(midia)

    def listar_midias(self,):
        print(f"\n--- midias na plataforma {self.nome} ---")
        for midia in self.lista_de_midias:
            print(midia.mostrar_info())

    def reproduzir_todas(self):
        print(f"\n --- iniciando reproduções automaticas---")
        for midia in self.lista_de_midias:
            midia.reproduzir()
