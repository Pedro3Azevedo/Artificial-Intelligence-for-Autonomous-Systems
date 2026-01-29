from pee.melhor_prim.aval.avalheur import AvalHeur

'''Este avaliador retorna o valor da função heuristica, que é uma estimatica do percuros do nó dado até ao no objetivo'''
class AvalSofrega(AvalHeur):
    def prioridade(self, no):
       return self._heuristica.h(no.estado)