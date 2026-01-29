"""
A Resposta, é a segunda parte de uma reação, que acontece depois de se detectar e haver um estimulo,
e depois de avaliado a sua intensidade, vai se opter uma resposta. Esta resposta, dependendo da intencidade
do estimulo da percecao, ativara uma certa ação.
Ou seja, class Resposta, tem a função de ativar uma ação, apartir da sua função "activar", 
que recebe a percepcao e a intensaidade proveniente do estimulo. É atribuido uma proridade da accao, com 
a intencidade recebida, e de seguida, é returnada essa accao, para ser ativada.
"""
class Resposta():
    '''Construtor da class Resposta, onde contem a accao que vai ser ativada.'''
    def __init__(self, accao):
        self._accao = accao

    '''
    é definida uma prioridade apartir da intensidade, e devolve a accao
    '''
    def activar(self, percepcao, intensidade=0):
        self._accao.prioridade = intensidade
        return self._accao