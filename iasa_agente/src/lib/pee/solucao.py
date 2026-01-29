'''A class solução contem o último nó do percuso final, o percuso que chega ao objetivo'''
from pee.passodolucao import PassoSolucao

'''A class solução contém o nó finaç que contem o estado objetivo e no seu construto faz o percurso do nó final até à raiz
Que será a solução do problema.'''
class Solucao():
    def __init__(self, no_final):
        self._no_final = no_final # ultimo no do percurso
        self._percurso = list()
        self._percurso.insert(0, self._no_final)
        no = no_final
        while no.antecessor:
            self._percurso.insert(0, no.antecessor)
            no = no.antecessor
            



    '''A dimensão, é o numero de nós que contém o percurso'''
    @property
    def dimensao(self):
        return len(self._percurso)

    '''O custo, é o custo do ultimo nó, que será a soma de todos os custos do percurso'''
    @property
    def custo(self):
        return self._percurso[-1].custo if self._percurso else 0

    '''Remove um passo do percurso
    Implica o obter o estado do no anterior e o operador do no seguinte'''
    def remover_passo(self):
        if self.dimensao > 1:
            estado_no = self._percurso[0].estado
            self._percurso.pop(0)
            operador_seguinte = self._percurso[0].operador
            return PassoSolucao(estado_no, operador_seguinte)


    '''Função para iterar o percurso que chega ao objetivo'''
    def __iter__(self):
        return iter(self._percurso)

    '''key=index
        Esta função retorna o nó numero key, que pertence ao percurso 
    '''
    def __getitem__(self, index):
        return self._percurso[index]