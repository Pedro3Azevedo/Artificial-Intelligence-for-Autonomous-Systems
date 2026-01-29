from mod.estado import Estado

''' O estado agente é um estado que corresponde a posicao do agente, caso este se encontre neste estado'''
class EstadoAgente(Estado):
    '''receve um tuplo da posiçao (x, y'''
    def __init__(self, posicao):
        self._posicao = posicao

    '''Posição do estado'''
    @property
    def posicao(self):
        return self._posicao

    ''' faz um hash da posição que é o id do estado, cada posição esta presente num unico estado'''
    def id_valor(self):
        ''''''
        return hash(self._posicao)