from abc import ABC, abstractmethod

'''A função heuristica representa uma estimativa do custo do percurso desde um nó até ao objetivo.
Reflete conhecimente«o acerca do dominio do problema para assim guiar a procura.
'''
class Heuristica(ABC):
    @abstractmethod
    def h(estado):
        '''return double'''