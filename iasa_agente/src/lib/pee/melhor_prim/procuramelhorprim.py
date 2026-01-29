from abc import ABC, abstractmethod
from pee.mec_proc.procuragrafo import ProcuraGrafo
from pee.melhor_prim.fronteiraprioridade import FronteiraPrioridade

'''Neste método de procura de Melhor-Primeiro, tira partido de uma avaliação do estado,
utilizando uma função para avaliar cada nó.
Por isso é utilizado uma fronteira onde o proximo nó a ser analisado é melhor( Quanto menor mais promissor é o nó).
 '''
class ProcuraMelhorPrim(ProcuraGrafo, ABC):
    def iniciar_fronteira(self):
        return FronteiraPrioridade(self.iniciar_avaliador())
    
    '''Para colocar o nó no dicionario de nós explorados e para adicionar a fronteira, o nó ainda não pode estar nos explorados,
    ou caso já esteja nos explorados, tem que ter um custo menor
    '''
    def manter(self, no):
       return super().manter(no) or  no.custo < self._explorados.get(no.estado).custo

            

    @abstractmethod
    def iniciar_avaliador(self):
        ''''''