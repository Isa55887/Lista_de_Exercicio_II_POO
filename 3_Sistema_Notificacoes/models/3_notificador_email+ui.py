class NotificadorEmail(Notificador):
    def notificar(self, mensagem):
        print(f"E-mail: {mensagem}")  # [UI]
