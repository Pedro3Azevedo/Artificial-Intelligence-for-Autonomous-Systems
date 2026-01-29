from abc import ABC
from pee.melhor_prim.procuramelhorprim import ProcuraMelhorPrim

'''Um metodos de Procura informada, são estratégias de exploração do espaço de estados,
tiram partidam de conhecimento do domínio do problema para ordenar a fronteira de exploração.
No método resolver é criada a variavel heuristica que vai ser usada para quando se iniciar cada avaliador.
É retornado a resolver da super classe.
'''
class ProcuraInformada(ProcuraMelhorPrim, ABC):
    def resolver(self, problema, heuristica):
        '''''' 
        self._heuristica = heuristica
        return super().resolver(problema)