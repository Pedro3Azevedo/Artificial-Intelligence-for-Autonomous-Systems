from abc import ABC


class SelAccao(ABC):
    '''Classe que seleciona a ação a executar, dependendo da aprendizagem
        a forma de selecionar a ação pode ser diferente, pode haver mais do que uma forma 
        de selecionar a ação.
    '''
    def selecionar_accao(self, s):
        '''return accao'''