from pee.melhor_prim.aval.avalaa import AvalAA
from pee.melhor_prim.informada.procurainformada import ProcuraInformada

'''Neste método de procura informada, a função a conparar entre percurso é,
a soma entre o custo do percurso explorado com a função heuristica, ou seja,
 a estimativa do custo do percurso até ao objetivo. 
 
 Temos aqui uma Heuristica admissivel. Uma heuristica admissivel é optimista, 
 a estimativa de custo é sempre inferior ou igual ao custo efectivo minimo. 
 Sabemos que, quanto mais perto do objetivo, menor é o valor da função heuristica, 
 ou seja, quanto mais afastado do objetivo, maior é o valor.

 Uma heuristica admissivel é obtida através da remoção de restrições associadas ao problema.


O método de procura A*, garante uma solução ótima e é completa.

Porém, este método não resolve todos os problemas. Pois podem não produzir soluções em tempo real. 
Por isso tem que se abdicar de ter uma solução otima, e utilizar o método de procura por Sôfrega

No método de iniciar avaliadorm é chamado o avaliador passando como atributo a heuristica passada no método resolver
 '''
class ProcuraAA(ProcuraInformada):
    def iniciar_avaliador(self):
        '''''' 
        return AvalAA(self._heuristica)