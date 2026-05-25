class NotificadorSMS(Notificador):
    def notificar(self, mensagem):
        print(f"SMS: {mensagem}")    # [UI]
