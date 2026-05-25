class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem):
        pass

class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        print(f"E-mail: {mensagem}")   # [UI]

class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        print(f"SMS: {mensagem}")    # [UI]

class NotificadorApp(Notificador):
    def notificar(self, mensagem):
        print(f"Notificação no APP: {mensagem}")   # [UI]
