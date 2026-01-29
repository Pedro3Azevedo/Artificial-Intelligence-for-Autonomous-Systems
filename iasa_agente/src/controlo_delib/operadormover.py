import math
from mod.agente.estadoagente import EstadoAgente
from mod.operador import Operador
from sae.agente.accao import Accao


class OperadorMover(Operador):
    
    def __init__(self, modelo_mundo, direccao):
        ''''''
        self._modelo_mundo = modelo_mundo
        self._ang = direccao.value
        self._accao = Accao(direccao)

    @property
    def ang(self):
        return self._ang

    @property
    def accao(self):
        return self._accao

    '''Para aplicar um estado, primeriro calcula se o x e o y do novo estado, apartir do passo,
     que esta no atributo da accao, multiplicando pelo cosseno e o seno (respetivamente) do angulo guardado.
     quando se optem a possiçao do novo estado, cria se o mesmo e verifica se este pertence aos estados existentes
     no Modelo do Mundo. '''
    def aplicar(self, estado):
        x, y = estado.posicao
        dx = round(self._accao.passo * math.cos(self._ang))
        dy = -round(self._accao.passo * math.sin(self._ang))
        pos = x+dx, y+dy
        novo_estado = EstadoAgente(pos)
        if novo_estado in self._modelo_mundo.estados():
            return novo_estado
        else:
            return None

    #Custo é porpocional a distancia entre o estado e o novo estado, caso este seja menor que 1,
    # o custo fica a 1
    def custo(self, estado, novo_estado):
        ''''''
        return max( math.dist(estado.posicao, novo_estado.posicao), 1)
    