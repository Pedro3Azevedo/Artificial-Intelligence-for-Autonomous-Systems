from controlo_react.reaccoes.evitar.evitardir import EvitarDir
from controlo_react.reaccoes.evitar.respostaevitar import RespostaEvitar
from ecr.hierarquia import Hierarquia

from sae.ambiente.direccao import Direccao

'''
    Nesta classe, é criada as reações possiveis de evitar objetos, que é evitar pelas diferentes direções.
    É criada uma instancia RespostaEvitar, para fornecer a reação.
'''
class EvitarObst(Hierarquia):
    def __init__(self):
        resposta = RespostaEvitar()
        super().__init__([
            EvitarDir(direccao, resposta) for direccao in list(Direccao) #Foi usado esta função para não haver redundancia, escolha por intencao
        ])