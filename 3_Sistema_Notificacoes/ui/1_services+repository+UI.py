class CentralNotificacoes:
    def __init__(self):
        self.notificadores = []   # [REPOSITÓRIO]: Armazenamento em memória

    def  adicionar_notificador(self, notificador):   # [SERVICES / REPOSITÓRIO]: Lógica para salvar um novo meio de envio
        self.notificadores.append(notificador)
    
    def enviar_para_todos(self, mensagem):   # [SERVICES + UI]: Comanda o envio e exibe os resultados na tela
        for notificador in self.notificadores:
            notificador.notificar(mensagem)
