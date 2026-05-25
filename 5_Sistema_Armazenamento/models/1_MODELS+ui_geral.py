class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado):
        pass
        
class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado):
        print(f"salvo {dado} em arquivo local")   # [UI]

class ArmazenadorBanco(Armazenador):
    def salvar(self, dado):
        print(f"salvo {dado} no banco de dados")   # [UI]

@runtime_checkable
class Salvavel(Protocol):
    def salvar(self, dado: str) -> None:
        ...

class ArmazenadorNuvem:
    def salvar(self, dado):
        print(f"salvo {dado} na nuvem")   # [UI]
