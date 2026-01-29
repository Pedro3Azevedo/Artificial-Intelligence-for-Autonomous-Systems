from abc import ABC, abstractmethod

from pee.mec_proc.no import No
from pee.solucao import Solucao
'''
    Um mecanismo de procura é uma exploração sucessiva do espaço de estados.
    Sendo que cada estado é representado por um nó , existe uma estado de procura de nós.
    é então realizada uma árvore de procura que corresponde a exploração dos nos e das sua possibilidades de transição de estado(estado sucessor)
    pelo que a raíz da árvore é o nó correspondente ao estado inicial.
    Por fim, tem se um fronteira de exploração, que é uma estrutura de dados com relações de ordem, 
    onde o criterio de ordenação, determina estratégia de controlo da procura. Árvore corresponde aos nós sucessores da raiz e assim sucessivamente,
    A forma de explorar os nós sucessores muda dependendo do mecanismo.  '''
class MecanismoProcura(ABC):
    def __init__(self):
        self._fronteira = None
        self._nosProcessados = 0
        self._nosEmMemoria = 0

    @property
    def nosProcessados(self):
        return self._nosProcessados

    @property
    def nosEmMemoria(self):
        return self._nosEmMemoria


    '''função que resolve o problema e devolve uma solução '''
    def resolver(self, problema):
        no = No(problema.estado_inicial)
        self._fronteira = self.iniciar_fronteira()
        self.memorizar(no)
        while not self._fronteira.vazia():
            no = self._fronteira.remover()
            if problema.objectivo(no.estado):
               return Solucao(no)
            self._nosProcessados += 1
            for child in self.expandir(problema, no):
                self.memorizar(child)
        return None

    '''método que cria uma fronteira de nós que guarda os nós sucessores que ainda não foram explorados.'''
    @abstractmethod
    def iniciar_fronteira(self):
        ''''''
    ''' O método expandir vai aplicar o operador ao estado do nó onde vai, com a função yield, acumular os estados sucessores dos estados sucessores
    para cada sucessor vai se aplicar o metodo memorizar'''
    def expandir(self, problema, no):
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            if estado_suc:
                #self._nosProcessados += 1
                yield No(estado_suc, operador, no)


    '''O m+etodo memorizar vai inserir os nos sucessores na fronteira, mas 
    dependendo do mecanismo de procura, vai ser verificado certas condiçoes para ver se o nó é inserido na fronteira, 
    e se for o casom é inserido'''
    @abstractmethod
    def memorizar(self, no):
        ''''''

