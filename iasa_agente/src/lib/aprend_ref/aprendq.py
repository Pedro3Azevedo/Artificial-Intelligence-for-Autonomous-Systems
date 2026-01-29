from aprend_ref.apredref import ApredRef



''''Para efeitos de execução, usamos o a' seguinte, para aprendizagem,
é usado o a' que maximiza'''

'''
Nesta aprendizagem, estima se o retorno, considerando a ação seguinte como a melhor
para a estimativa do Q do estado e ação seguintes.
'''
class AprendQ(ApredRef):
    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        #super().__init__(mem_aprend, sel_accao)
        self._sel_accao = sel_accao
        self._mem_aprend = mem_aprend
        self._alfa = alfa
        self._gama = gama
    
    '''Neste metodo de aprendizagem, Q-learning, para atualizar o Q(s,a), vai se ver as açoes em memoria, 
    e vai se escolher aquela que vai dar o caminho otimo'''
    def aprender(self, s, a, r, sn):
        ''''''
        an = self._sel_accao.accao_sofrega(sn) #ação seguinte no estado seguinte
        qsa = self._mem_aprend.q(s, a) #valor q para o estado e a ação presnete
        qsnan = self._mem_aprend.q(sn, an) #valor para o estado e acao seguinte, ação que é a que maximiza este q
        q = qsa +self._alfa * (r + self._gama * qsnan - qsa)
        self._mem_aprend.atualizar(s, a, q) 
        ''' Ou seja, o valor do q a ser atualizado para o estado e ação atual, 
        é o valor atual do q do estado ação presente, mais alfa vezes do reforço recebido da ação,
        mais gama vezes o q do próximo estado e da proxima ação, ação esta que é escolhida atraves da accao sofrega, ou seja, 
        a ação qur maximiza o q, menos o q do estado e ação atual.'''



    