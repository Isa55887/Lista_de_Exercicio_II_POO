from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass

class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        print(f"E-mail: {mensagem}")

class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        print(f"SMS: {mensagem}")

class NotificadorApp(Notificador):
    def notificar(self, mensagem):
        print(f"Notificação no APP: {mensagem}")

class CentralNotificacoes:
    def __init__(self):
        self.notificadores = []

    def  adicionar_notificador(self, notificador):
        self.notificadores.append(notificador)
    
    def enviar_para_todos(self, mensagem):
        for notificador in self.notificadores:
            notificador.notificar(mensagem)
