from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

'''
    Vai detectar um estimulo numa certa direção que vai ser esta direcao vai ser guardada
'''
class EstimuloAlvo(Estimulo):
    def __init__(self, direccao, gama=0.9):
        self._direccao = direccao
        self._gama = gama

    '''Nesta função, detecta se o elemento e a distancia a esse elemento da percepção na direção guardada.
    Caso exista um alvo , a função vai devolver a intensidade da percepção, quanto mais perto do alvo, mais intensidade há.
    Pois, o objetivo é o agente ir ao alvo mais perto, se ele percepcionar vários alvos em diferentes direções vai ao mais perto.
    '''    
    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self._direccao]
        if elemento == Elemento.ALVO:
            return self._gama**distancia
        return 0