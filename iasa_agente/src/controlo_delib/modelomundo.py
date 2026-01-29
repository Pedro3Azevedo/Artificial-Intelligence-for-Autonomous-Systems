''''''
from controlo_delib.operadormover import OperadorMover
from mod.agente.estadoagente import EstadoAgente
from plan.modeloplan import ModeloPlan
from sae.ambiente.direccao import Direccao

'''Classe que representa o espaço onde o agente se encontra. 
Este espaço é constituido por elementos como obstaculos e alvos, 
e tem guardado aos estados presentes e os operadoes, neste caso OperadorMover.
Nesta Classe tem um metodo que atualiza os seus elementos e atributos, e outra que 
mostra o espaço, o mundo onde se encontra o agente
'''

class ModeloMundo(ModeloPlan):
    
    def __init__(self):
        ''''''
        self._operadores = [OperadorMover(self, direccao) for direccao in Direccao]
        self._estado = None
        self._estados = list()
        self._alterado = False
        self._elementos = {}

    '''Atributo que representa se o modelo do mundo foi alterado'''
    @property
    def alterado(self):
        return self._alterado    

    #Os elementos podem ser Alvos, Obstaculos, Agentes ou vazio. 
    # Este dicionario correspode aos elemetos presentes  no modelo do mundo,
    # cuja a key é a posição desses elementos no ambiente.
    @property
    def elementos(self):
        return self._elementos

    '''Neste método, altera se o estado e de seguida, verifica se se os elementos na percepcao são iguais 
    aos elementos do Modelo do Mundo. Caso sejam diferentes, atualiza se 
    os elementos do Modelo do Mundo, com os elementos da percepcao
    e altera se os estados do Modelo do Mundo, criando novos estados agente 
    com as posiçoes da percpcao. coloca se a cariavel alterado para true.
    '''
    def actualizar(self, percepcao):
        self._estado = EstadoAgente(percepcao.posicao)
        if percepcao.elementos != self._elementos:
            self._elementos = percepcao.elementos
            self._estados = [EstadoAgente(pos)
                             for pos in percepcao.posicoes]
            self._alterado = True
        else:
            self._alterado = False

    '''Estado atual do agente'''
    def estado(self):
        return self._estado

    '''Estados presentes no modelo do mundo'''
    def estados(self):
        return self._estados

    '''Operadores que contem ações '''
    def operadores(self):
        return self._operadores

    '''Retorna se o elemento pertencente ao Modelo do Mundo cuja a posiçao seja igual
    a posicao do estado recebido'''
    def obter_elem(self, estado):
        return self._elementos.get(estado._posicao)
        
    '''Vai mostrar os obstaculos, alvos e a posicao do estado atual'''
    def mostrar(self, vista):
        vista.mostrar_alvos_obst(self._elementos)
        vista.marcar_posicao(self._estado.posicao)
        