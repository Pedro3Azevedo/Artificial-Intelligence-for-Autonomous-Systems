from aprend_ref.aprendq import AprendQ
from aprend_ref.memoriaesparsa import MemoriaEsparsa
from aprend_ref.selaccaoegreedy import SelAccaoEGreedy

'''Class fachada que vai ser usada para "esconder" a complexidade dos metodos, 
ou seja, esta classe delega as classes que agrega os metodos que seram executados
'''
class MecAprend():
    def __init__(self, accoes, alfa = 0.5, gama = 0.9, epsilon = 0.01):
        #gama valor de desconto como usado no procecsso de Makrov
        self._accoes = accoes
        self._alfa = alfa
        self._gama = gama
        self._epsilon = epsilon
        self._mem_aprend = MemoriaEsparsa()
        self._sel_accao = SelAccaoEGreedy(self._mem_aprend, accoes, epsilon)
        self._aprend_ref = AprendQ( self._mem_aprend, self._sel_accao, alfa, gama)
        

    @property
    def estados(self):
        return self._mem_aprend.obter_estados()

    '''Este método é delegado ao aprender do Lerning-Q'''
    def aprender(self, s, a, r, sn):
        return self._aprend_ref.aprender(s, a, r, sn)

    '''Este método é delegado ao selecionar ação do Selecao Acao Epsilon Greedy'''
    def selecionar_accao(self, s):
        return self._sel_accao.seleccionar_accao(s)

    '''Este método é delegado ao ação sofrega do Selecao Acao Epsilon Greedy'''
    def accao_sofrega(self, s):
        return self._sel_accao.accao_sofrega(s)
    
    '''Este metodo é delegado a MemoriaEsparsa '''
    def q(self, s, a):
        return self._mem_aprend.q(s, a)