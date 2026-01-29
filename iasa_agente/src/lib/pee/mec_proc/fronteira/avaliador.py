from abc import ABC, abstractmethod

'''Avalia o estado, através do custo, e  define a prioridade '''
class Avaliador(ABC):
    @abstractmethod
    def prioridade(self, no):
        ''''''