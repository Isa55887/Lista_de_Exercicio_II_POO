from questao4_lista2 import Imprimivel, Boleto, Etiqueta, RelatorioSimples, processar_impressao

boleto = Boleto("123.456", 450.00)
etiqueta = Etiqueta("isa", "jardim lorena, 123")
relatorio = RelatorioSimples("vendas mensais")

objetos = [boleto, etiqueta, relatorio]

for obj in objetos:
    processar_impressao(obj)
