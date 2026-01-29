from random import choice
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

from sae import Direccao

from ecr.comportamento import Comportamento


'''A classe explorar é uma reacção, logo é um comportamento.
Esta reação consiste em um agente mover se numa direção aleatória.
Então, na função ativar, é gerada uma direção aleatória
apartir do Enumerado de direções da biblioteca sae. Com esta direção cria se uma respostaMover que 
se pode ativar apartir da percepção, para assim o agenter mover se numa direção aleatória.'''
class Explorar(Comportamento):
    def activar(self, percepcao):
        direccao = choice(list(Direccao))
        resposta = RespostaMover(direccao)
        return resposta.activar(percepcao)
