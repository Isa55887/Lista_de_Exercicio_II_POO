from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado):
        pass
        
class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado):
        print(f"salvo {dado} em arquivo local")

class ArmazenadorBanco(Armazenador):
    def salvar(self, dado):
        print(f"salvo {dado} no banco de dados")

@runtime_checkable
class Salvavel(Protocol):
    def salvar(self, dado: str) -> None:
        ...

class ArmazenadorNuvem:
    def salvar(self, dado):
        print(f"salvo {dado} na nuvem")

def executar_salvamento_formal(armazenador: Armazenador, dado):
    armazenador.salvar(dado)

def executar_salvamento_flexivel(objeto: Salvavel, dado):
    objeto.salvar(dado)
