def executar_salvamento_formal(armazenador: Armazenador, dado):
    armazenador.salvar(dado)

def executar_salvamento_flexivel(objeto: Salvavel, dado):
    objeto.salvar(dado)
