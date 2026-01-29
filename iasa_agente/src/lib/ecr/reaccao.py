from .comportamento import Comportamento

'''
Uma ação é ativada apartir de uma perceção. Para provocar uma ação, é há uma percepçao,
 provocando uma reação, que por sua vez activa uma ação. 
 Uma reação é composta por um estimulo seguido de uma resposta. Primeiro, com a perceção,
 é detectado um estimulo com  uma certa intensidade. E com base nessa intensidade, é provocada
 uma resposta, ativando uma ação. Com isto, podemos dizer, que uma reação é um comportamento,
ativando uma accao. Uma Perceção pode ter varias reaçoes, correspondendo a uma diferente ação.

Esta classe Reaccao, portanto, implementa a interface Coportamento. Esta classe é composta pela 
classe abstrata estimulo, e a classe resposta, pelos motivos a cima indicados.
Como podemos ver, a função da classe vai ser, detetando uma perceção, ativar uma ação.'''
class Reaccao(Comportamento):
    def __init__(self, estimulo, resposta):
        self._estimulo = estimulo
        self._resposta = resposta
    
    '''
    A funçao seguinte, é a que executa o propósito desta classe, ou seja, ativa uma accao.
    É recebido como paramtro uma perceção, onde a partir da classe estimulo, é detetada dando uma certa intensidade.
    Com esta intensidade recebida pelo Estimulo, e no caso de esta ser maior que 0, é ativada uma ação, com a classe Resposta.

    Ou seja, existe uma perceção, que deteta um estimulo, atriuindo uma intensidade para provocar uma resposta, que,
    com o valor da intensidade, ativará uma ação.'''
    def activar(self, percepcao):
        intensidade = self._estimulo.detectar(percepcao)
        if intensidade > 0:
            accao = self._resposta.activar(percepcao, intensidade)
            return accao
