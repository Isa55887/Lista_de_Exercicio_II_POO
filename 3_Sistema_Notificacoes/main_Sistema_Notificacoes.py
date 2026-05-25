from questao3_lista2 import Notificador, NotificadorEmail, NotificadorSMS, NotificadorApp, CentralNotificacoes

central = CentralNotificacoes()

email = NotificadorEmail()
sms = NotificadorSMS()
app = NotificadorApp()

central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)

central.enviar_para_todos("oi! boa tarde.")

"""
Qual classe representa o contrato formal?
R = A classe que representa o contrato formal é a "Notificador", ao herdar de ABC e usar o @abstractmethod no método notificar, ela estabelece uma regra/contrato
para o sistema, qualquer nova classe que queira ser um notificador válido é obrigada a implementar o método notificar(self, mensagem).

Onde há polimorfismo?
R = O polimorfismo ocorre dentro da classe CentralNotificacoes, no método enviar_para_todos ("print(i.notificar(mensagem))")

Por que faz sentido usar ABC nesse caso?
R = Faz sentido porque um Notificador é apenas um conceito abstrato, no sistema não existe um envio de mensagem "genérico"; uma notificação real precisa 
obrigatoriamente de um canal físico (como um e-mail, um SMS ou um alerta de aplicativo).

O que aconteceria se uma subclasse de Notificador não implementasse notificar()?
R = Se eu criasse uma nova subclasse, por exemplo class NotificadorWhatsApp(Notificador), e esquecesse de escrever o método notificar dentro
dela, o Python impediria a criação do objeto.
"""
