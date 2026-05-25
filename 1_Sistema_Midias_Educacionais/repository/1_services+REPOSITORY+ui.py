class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.lista_de_midias = []   # [REPOSITÓRIO]: Armazenamento local dos dados em memória

    def adicionar_midia(self, midia):   # [SERVICES / REPOSITÓRIO]: Lógica para manipular os dados (salvar na lista)
        self.lista_de_midias.append(midia)

    def listar_midias(self):   # [SERVICES + UI]: Comanda a lista e usa o print para exibir na tela
        print(f"\n--- midias na plataforma {self.nome} ---")
        for midia in self.lista_de_midias:
            print(midia.mostrar_info())

    def reproduzir_todas(self):   # [SERVICES + UI]: Comanda o fluxo de execução e exibe mensagens de erro e sucesso
        print(f"\n --- iniciando reproduções automaticas---")
        for midia in self.lista_de_midias:
            midia.reproduzir()
