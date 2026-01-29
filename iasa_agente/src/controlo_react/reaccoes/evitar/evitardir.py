from controlo_react.reaccoes.evitar.estimuloobst import EstimuloObst
from ecr.reaccao import Reaccao


'''Esta classe representa a reação de evitar uma direção, tendo como estimulo a classe EstimuloObstaculo e a resposta é fornecida
esta resposta é RespostaEvitar, que vai fazer com que o agente evite o objeto movendo se para outra direção'''
class EvitarDir(Reaccao):
    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObst(direccao), resposta)