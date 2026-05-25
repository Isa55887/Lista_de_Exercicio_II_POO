from questao5_lista2 import Armazenador, ArmazenadorArquivo, ArmazenadorBanco, Salvavel, ArmazenadorNuvem, executar_salvamento_formal, executar_salvamento_flexivel

arq = ArmazenadorArquivo()
db = ArmazenadorBanco()
nuvem = ArmazenadorNuvem()

executar_salvamento_formal(arq, "dados 1")
executar_salvamento_flexivel(nuvem, "dados 2")
