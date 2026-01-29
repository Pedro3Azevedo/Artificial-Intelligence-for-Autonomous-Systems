from abc import ABC


class ModeloPDM(ABC):

    '''Conjunto de estado do mundo'''
    def S(self):
        '''Return List<Estado>'''
    
    '''conjunto de acçoes possiveis no estado s
    s pertence ap conjunto de estados do mundo'''
    '''s-Estado'''
    def A(self, s):
        '''Return List<Operador>'''

    '''Funçao transiçao, da a probabilidade de transição
        porbabilidade de transição do estado spara s' atraves do operador a
    '''
    '''s-Estado, a-Operador'''
    def T(self, s, a):
        '''Return List<Transicao>'''

    '''Recompensa esperada na transicao do estado s para o estado s'
        atraves do operador a
    '''
    '''s-Estado, a-Operador, sn-Estado'''
    def R(self, s, a, sn):
        '''return double'''