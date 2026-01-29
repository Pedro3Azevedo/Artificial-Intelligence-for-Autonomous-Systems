from abc import ABC, abstractmethod

'''Para Representar um problema, existe um modelo.
    Esta modelo é constituido por um estado inicial, operadores e objectivos.
    Para alcançar os obejetivos, aplica se operadores ao estado inicial e aos estados seguintes 
    até chegar ao objectivo.

    Um estado é uma configuração ou situação qna resolução de um problema. 
    Para transitar entre estados são usados operadores que sã ações.
    '''
class Problema(ABC):
    
    '''Esta classe guarda duas variáveis, o estado_inicial, que representa o estado inicial do problema, que é privada.
        e a variavel operadores que representa o conjunto de transações, operadores que se pode executar no problema.
        '''
    def __init__(self, estado_inicial, operadores):
        self._estado_inicial = estado_inicial
        self._operadores = operadores

    '''método para ler a lista de operadores do problema, que é privada.'''
    @property
    def operadores(self):
        return self._operadores

    '''método para ler o estado inicial do problema, que é privada.'''
    @property
    def estado_inicial(self):
        return self._estado_inicial

    '''Objectivo do problema, retorna boolean
            Este método recebe um estado e verifica se este é o estado objetivo do problema
    '''
    @abstractmethod
    def objectivo(self, estado):
        ''''''