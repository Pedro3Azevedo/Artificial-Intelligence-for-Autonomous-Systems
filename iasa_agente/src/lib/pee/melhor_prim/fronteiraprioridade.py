from pee.mec_proc.fronteira.fronteira import Fronteira

from heapq import heappush, heappop


'''Nesta fronteira é criada a ordem por prioridade e ao remover, remove o nó com menor prioridade'''
class FronteiraPrioridade(Fronteira):
    '''priority queue'''

    def __init__(self, avaliador):
        super().__init__()
        self.avaliador = avaliador

    '''é avaliado a prioridade do nó, recebendo um double, e usando o heappush, coloca o nó na lista na ordem de prioridade'''
    def inserir(self, no):
        heappush(self._nos, (self.avaliador.prioridade(no), no))

    '''é retornado o nó com menor prioridade'''
    def remover(self):
        _, no = heappop(self._nos)
        return no
