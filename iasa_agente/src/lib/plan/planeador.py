from abc import ABC, abstractmethod

class Planeador(ABC):
    
    '''método que vai criar o problema , a heuristica(caso necessario)  e com esses dados
    aplica a funcao resolver do metodo de procura, o que ira dar uma solucao'''
    @abstractmethod
    def planear(self, modelo_plan, objectivos ):
        ''''''

    '''metodo que vai executar a solução, ou seja, vai avançar na lista do percurso
    até chegar ao objetivo final. Utiliza o remover_passo da class solucao para essa etapa
    do percurso sair da lista apos ser avançado '''
    @abstractmethod
    def obter_accao(self, estado):
        '''return Operador'''

    '''Verificar se o plano é valido, ou seja, se existir um plano(uma solução) e se,
    o estado onde o agente se encontra é o mesmo que o estado do proximo pass da solução'''
    @abstractmethod
    def plano_valido(self, estado):
        '''return boolean'''

    '''Termina o plano, colocando a solucao a None'''
    @abstractmethod
    def terminar_plano(self):
        ''''''