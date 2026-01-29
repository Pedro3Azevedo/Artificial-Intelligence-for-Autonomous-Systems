
from controlo_react.reaccoes.aproximar.estimuloalvo import EstimuloAlvo
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao


'''Esta classe represenata uma reação onde vai aproximar por uma direção
    É usado a class EstimuloAlvo como estimulo da reaçao e a class RespostaMover como resposta
    apartir do estimulo é criada uma resposta para executar uma accao, neste caso a açao vai ser mover par a direçao
    '''
class AproximarDir(Reaccao):
    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))