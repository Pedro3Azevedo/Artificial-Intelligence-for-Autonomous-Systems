from .comportamento import Comportamento
from abc import ABC, abstractmethod

'''
     Esta classe, que é composta por comportamentos, vai ativar uma certa accao.
     Para isso, esta classe contém uma lista de comportamentos que podem conter uma accao
     e se esse for o caso, é ativada e depois é adicionada numa lista para esta ser uma opção
    de escolha de accao.
'''
class ComportComp(Comportamento, ABC):
    '''No construtor desta class, é fornecido uma lista de comportamentos,
    onde a classe vai guardar a lista.'''
    def __init__(self, comportamentos):
        self._comportamentos = comportamentos

    '''Neste método, vai se ativar as accoes de cada comportamento, por isso,
        percorre-se todos os comportamentos da lista e, caso haja uma ação, 
        utilizar a função ativar o comportaento introduzindo a perceção recebia,
        adiciona se a uma lista de ações para depois ser selecionada uma delas.
    '''
    def activar(self, percepcao):
        accoes = list()
        for comportamento in self._comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
                accoes.append(accao)
        if accoes:
            return self.selecionar_accao(accoes)
    
    '''método abstracto que, nas classes que utilizarem, vai escolher de uma lista de accoes,
    uma accao, haverá várias forma de selecionar'''
    @abstractmethod
    def selecionar_accao(accoes):
        ''''''

