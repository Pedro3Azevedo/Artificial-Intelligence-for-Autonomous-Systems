from pee.melhor_prim.aval.avalheur import AvalHeur

'''Este avaliador vai retornar o valor da soma entre a função heuristica(que é uma estimatica do percuros do nó dado até ao no objetivo)
 com o valor do custo do percurso dos nós explorados'''
class AvalAA(AvalHeur):
    def prioridade(self, no):
        return self._heuristica.h(no.estado) + no.custo
