from abc import ABC, abstractmethod

'''Um Operador representa um ação, quando aplicado uma ação, o estado é alterado.
Ou seja, o operador gera uma trasformação de estado '''
class Operador(ABC):

    '''Aplicar um operador a um estado, gera um novo estado'''
    @abstractmethod
    def aplicar(self, estado):
        ''''''

    '''cada operador tem um custo, recebe um estado, e o estado sucedor.
     Este método devolve o custo necessario para transitar para o proximo estado
     neste método será o custo do estado mais o do estado sucessor
     '''
    @abstractmethod
    def custo(self, estado, estado_suc):
        ''''''