

'''
    A classe Recolher vai ser constituida por 3 comportamentos, o aproximar, o evitar e o explorar.
    Esta classe é uma hierarquia, um comportamento composto, logo é usado o construtor da class ComportComp
    onde se é dado uma lista de comportamentos que corresponde a esta ação.
'''
from controlo_react.reaccoes.aproximar.aproximaralvo import AproximarAlvo
from controlo_react.reaccoes.evitar.evitarobst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar
from ecr.hierarquia import Hierarquia


class Recolher(Hierarquia):
    def __init__(self):
       super().__init__([
           AproximarAlvo(), 
           EvitarObst(),
           Explorar()
        ]) 