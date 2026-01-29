from controlo_react.reaccoes.aproximar.aproximardir import AproximarDir
from ecr.prioridade import Prioridade
from sae import Direccao

'''A classe AproximarAlvo, vai ser um comportamento composto sende que a ordem é a de prioridade.
Este conjunto de comportamentos, sao reações que vao ser AporoximarDirecao onde vai aproximar por Norte, Sul, Este ou Oeste.
Para isto é criado uma lista com as reaccoes de aproximar para cada direccao.
'''
class AproximarAlvo(Prioridade):
    def __init__(self):
        super().__init__([
            AproximarDir(direccao) for direccao in list(Direccao) #Foi usado esta função para não haver redundancia, escolha por intencao
        ])

    