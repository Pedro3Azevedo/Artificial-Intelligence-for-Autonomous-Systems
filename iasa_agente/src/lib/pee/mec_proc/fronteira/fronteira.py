from abc import ABC, abstractmethod

'''Uma fronteira é um conjunto de nós que vai determinar a estratégia de controlo de procura.
Esta classe é constituida por uma lista de nós onde o modo de insereção do nó vai depender do tipo de fronteira.
'''
class Fronteira(ABC):
    def __init__(self):
        self._nos = list()

    '''verificar se a lista de nos esta vazia'''
    def vazia(self):
        return len(self._nos) == 0

    '''Neste método vai ser introduzido um nó'''
    @abstractmethod
    def inserir(self, no):
        ''''''
    
    '''nesta método é removido um nó'''
    def remover(self):
        return self._nos.pop(0)
