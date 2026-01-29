'''Um nó representa um estado, que é uma etapa da procura.
   Cada nó tem um operador associado e tambem tem um nó antecedor,
   o que faz co que este tenho um grau de profundidade. Para além disto tem um custo associado
'''
class No():
    '''Um nó vai conter a informação do estado, do operador (que faz a transição do estado para outro),
    a informação do antecessor, a profundidade a que está, imaginando numa árvora, se for o nó inicial, é 0,
    caso contrario, será a profundidade do nó antecedor mais 1. por fim, guarda o custo, que é a soma do custo do antecessor mais o custo do operador
    Se o nó for o primeiro, não terá custo associado. '''
    def __init__(self, estado, operador=None, antecessor=None):
        self._estado = estado
        self._operador = operador
        self._antescessor = antecessor
        if not operador and not antecessor:
            self._profundidade = 0
            self._custo = 0
        else:
            self._profundidade =antecessor.profundidade + 1
            self._custo = antecessor.custo + operador.custo(antecessor.estado, estado)
 
    @property
    def profundidade(self):
        return self._profundidade
    @property
    def custo(self):
        return self._custo

    @property
    def estado(self):
        return self._estado

    @property
    def operador(self):
        return self._operador

    @property
    def antecessor(self):
        return self._antescessor

    '''less than'''
    def __lt__(self, no):
        return self.custo < no.custo