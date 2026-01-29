from abc import ABC
from pee.mec_proc.mecanismoprocura import MecanismoProcura

'''A procura geral em grafos, vem resolver o problema de ter estados repetidos na árvore de procura.
    Então, para minimizar o desperdicio de recursos, de tempo e memória, ao gerar um nó sucessor
    vai se ter em consideração os seguintes pontos
        - no caso do no sucessor não pertenceraos nós abertos (nós gerados mas não expandidos ) e não pertencer aos nos fechados (nós expandidos)
            o nó sucessor vai ser inserido nos nós abertos (Fronteira de exploração)
        - no caso do nó sucessor pertencer aos nós abertos, se foi atingido através de um caminho mais curto, ou seja com menor custo,
            vai se remover o nó anterior em abertos (que tem maior custo) e insere se este nó nos abertos
        - port fim, caso o nó pertencer aos fechados, e se foi atingido através de um caminho mais curto,
            remove se dos Fechados e insere se em Abertos.
'''


class ProcuraGrafo(MecanismoProcura, ABC):
    '''Método vai usar o método da super classe, nos mecanismos de procura é tambem usado um dicionario que contem os nós que já foram exprorados.'''

    def resolver(self, problema):
        self._explorados = {}
        solucao = super().resolver(problema)
        self._nosEmMemoria = len(self._explorados)
        return solucao

    '''Para este método, no caso da condição se verificar, vai se adicionar o nó aos nós explorados e á fronteira.
     Só é adicionado no caso do nó não pertencer ao dicionário de nós explorados '''

    def memorizar(self, no):
        if self.manter(no):
            self._explorados[no.estado] = no
            self._fronteira.inserir(no)

    ''' '''

    def manter(self, no):
        return no.estado not in self._explorados
        
