from abc import ABC, abstractmethod

"""
    Um comportamento relaciona Padrões de percecao com Padroes de acao, ou seja,
    a partir de uma perceção, consegue se uma ação.
    Um comportamento, vai ativar uma accao, apartir de uma percecao.
    Um comportamento pode ser tanto uma reaccao como um comportamento composto

    Como podemos ver no metodo 'atictivar', é recebido uma percecao, e vai ser apartir desta 
    que se obterá uma accao.
"""
class Comportamento(ABC):
    @abstractmethod
    def activar(self, percepcao):
        """Provoca uma accao"""