from mod.operador import Operador
from abc import ABC, abstractmethod
'''
Um estado representa uma situação ou configuração na resolução de um problema.
Cada estado terá uma identificação diferente de todos os outros estados. 
A identificação do mesmo vai ser calculado por uma função hash.
'''
class Estado(ABC):
    @abstractmethod
    def id_valor(self):
        ''''''

    '''Fornece uma idenctificação unica'''
    def __hash__(self):
        return self.id_valor()
        

    '''Operador de igualdade, verifica se dois objectos são iguais'''
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()