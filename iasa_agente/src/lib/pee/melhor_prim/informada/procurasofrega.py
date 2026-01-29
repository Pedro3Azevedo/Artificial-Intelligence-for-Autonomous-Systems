from pee.melhor_prim.aval.avalsofrega import AvalSofrega
from pee.melhor_prim.informada.procurainformada import ProcuraInformada

'''Neste método de procura informada, a função que vai ser comparada entre caminhos é igual á função heuristica.
Não tem em conta o custo do percurso explorado, so a estimativa.
Minimiza o custo local. Porém pode não ser a melhor solução, ou seja, obtém se,
soluções suub-optimas.

No método de iniciar avaliadorm é chamado o avaliador passando como atributo a heuristica passada no método resolver
'''
class ProcuraSofrega(ProcuraInformada):
    def iniciar_avaliador(self):
        return AvalSofrega(self._heuristica)