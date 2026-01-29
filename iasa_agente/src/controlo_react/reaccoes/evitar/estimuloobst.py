
from ecr.estimulo import Estimulo
from sae import Elemento

'''Nesta classe vai se detetar uma perceção de uma certa direção para depois haver uma ação de evitar obstáculo
    No construtor é fornecido a direção para verificar a percepão nessa direção para ver se é necessário evitar algo
'''
class EstimuloObst(Estimulo):
    def __init__(self, direccao, intensidade=1):
        self._direccao = direccao
        self._intensidade = intensidade

    '''Nesta função, vai se detetar se o agente, numa certa direção, percepciona um objeto e vê se tem contacto com o mesmo.
    No caso de haver obstáculo e haja contacto com o mesmo, é returnado a intensidade para que o agente tenha uma resposta com a
    ação de evitar o obstaculo '''
    def detectar(self, percepcao):
        elemento, _ , _ = percepcao[self._direccao]
        if elemento == Elemento.OBSTACULO and percepcao.contacto_obst(self._direccao):
            return self._intensidade
        return 0