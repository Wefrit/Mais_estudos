from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> None:...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> float:
        print ('Enviando E-mail: ', self.msg)
        return 0.1
    
class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('Enviando SMS: ', self.msg)
        return True    

def notificar(notificacao: Notificacao):
    if notificacao.enviar():
        print('Notificação enviada')
    else:
        print('Foo')


notificar(NotificacaoSMS('teste'))