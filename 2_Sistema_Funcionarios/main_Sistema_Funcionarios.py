from questao2_lista2 import Funcionario, FuncionarioAssalariado, FuncionarioHosrista, FuncionarioComissado, Empresa

minha_empresa = Empresa("Dona Novinha")

f1 = FuncionarioAssalariado("Ana paula", "050.758.462-70", 1500)
f2 = FuncionarioComissado("Vicktor Eduardo", "044.896.972-60", 100, 1500 )
f3 = FuncionarioHosrista("isabely", "035.466.612-65", 12, 2000)

minha_empresa.adicionar_funcionario(f1)
minha_empresa.adicionar_funcionario(f2)
minha_empresa.adicionar_funcionario(f3)

minha_empresa.listar_funcionarios()
minha_empresa.mostrar_folha_de_pagamento()

"""
Qual é a superclasse da hierarquia?
R = A superclasse é "Funcionario"

Quais são as subclasses?
R = As subclasses são: "FuncionarioAssalariado", "FuncionarioHorista" e "FuncionarioComissionado"

Onde ocorre sobrescrita?
R = No método calcular_pagamento, este método é declarado como abstrato na superclasse e é sobrescrito dentro de cada uma das três
subclasses para realizar o cálculo específico de cada tipo de funcionario.

Onde ocorre polimorfismo?
R = O polimorfismo acontece dentro da classe "Empresa", especificamente no método mostrar_folha_pagamento (pagamento = i.calcular_pagamento())

Qual a vantagem de usar ABC nesse caso?
R = Garantia de um contrato, pois ao marcar calcular_pagamento com @abstractmethod, o Python obriga qualquer desenvolvedor que criar uma nova subclasse
de Funcionario a implementar esse método, se alguém esquecer de criá-lo, o código quebrará imediatamente, evitando erros em produção quando a classe
Empresa tentar rodar a folha de pagamento.

"""
