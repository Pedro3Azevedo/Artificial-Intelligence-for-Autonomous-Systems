from pee.mec_proc.no import No
from pee.prof.procuraprof import ProcuraProf
from abc import ABC


''' Este mecanismo de procura é o mesmo que o da classe ProcuraProfundidade, com o promenor de conter uma profundidade máxima.
Ou seja, com este método cai se estar a explorar os nós e a expand-los, até que a profundidade dos mesmos seje igual à profundidade máxima
Com este método, podemos não chegar a um objetivo.'''
class ProcuraProfLim(ProcuraProf, ABC):
    
    def resolver(self, problema, prof_max=1000):
        self._prof_max = prof_max
        return super().resolver(problema)
        
     
    '''Neste método expandir vai se verificar primeiro se já se ultrapassou a profundidade máxima
    Ainda antes de expandir como a superclasse, ainda é verificado se o nó esta repetido, para evitar um ciclo.'''
    def expandir(self, prolema, no):
        if no.profundidade > self._prof_max:
            return
        elif not self.isCycle(no):
            yield from super().expandir(prolema, no)

    '''Método que percorre os nós antecessores para verificar se o nó a ser analisado está repetido.'''
    def isCycle(self, no):
        no_ante = no.antecessor
        while  no_ante:
            if no_ante == no:
                return True
            no_ante = no_ante.antecessor
        return False
    