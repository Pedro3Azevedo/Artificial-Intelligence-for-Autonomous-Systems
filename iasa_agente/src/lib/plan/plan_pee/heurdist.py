import math
from pee.melhor_prim.aval.heuristica import Heuristica
'''Heuristivca que calcura a distancia entrw a posicao do estado com a posicao do estado atual'''
class HeurDist(Heuristica):

    def __init__(self, estado_final):
        self._estado_final = estado_final

    def h(self, estado):
        return math.dist(estado.posicao, self._estado_final.posicao)