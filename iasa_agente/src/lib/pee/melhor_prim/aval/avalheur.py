from abc import ABC
from pee.mec_proc.fronteira.avaliador import Avaliador


'''Avaliadores que utilizam uma função heuristica. '''
class AvalHeur(Avaliador, ABC):
    '''Guarda a funçao heuristica que o avalidor vai usar'''
    def __init__(self, heuristica):
        self._heuristica = heuristica