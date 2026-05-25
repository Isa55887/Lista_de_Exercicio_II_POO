class ArmazenadorBanco(Armazenador):
    def salvar(self, dado):
        print(f"salvo {dado} no banco de dados")  # [UI]
