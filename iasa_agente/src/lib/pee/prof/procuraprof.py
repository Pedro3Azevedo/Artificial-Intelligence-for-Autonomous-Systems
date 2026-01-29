from pee.mec_proc.mecanismoprocura import MecanismoProcura
from abc import ABC

from pee.prof.fronteiraLIFO import FronteiraLifo

'''Neste método de procura de controlo explora se os nós mais recentes, utiliza a fronteira Last in First out 
Ou seja, neste mecanismo de procura vai se analisar sempre o nó 'filho', está se sempre a ir mais fundo.

Para esse efeito é usada a fronteira do tipo Last in First out.
Neste método não é necessário guardar os estados dos nos explorados e não gasta tanta memoria com a procura melhor-primeiro.
Porém tem o risco de não encontrar a solução
'''
class ProcuraProf(MecanismoProcura, ABC):
    def iniciar_fronteira(self):
        return FronteiraLifo()
    
    def memorizar(self, no):
        self._fronteira.inserir(no)
        if(self._nosEmMemoria < len(self._fronteira._nos)):
            self._nosEmMemoria =len(self._fronteira._nos)
        
        #Colocar na fronteira
