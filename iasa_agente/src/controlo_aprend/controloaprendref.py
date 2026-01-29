from controlo_aprend.mecaprend import MecAprend
from mod.agente.estadoagente import EstadoAgente
from sae import Controlo
from sae.agente.accao import Accao
from sae.ambiente.direccao import Direccao

'''
Este tipo de controlo utiliza uma aprendizagem por reforço.
Desta forma, o agente não conhece o mundo, o que fará com que este tenha que explorar.
O agente vai aprendendo como chegar ao objetivo.

Para não ficar muito complexo, é criado uma classe fachada que vai agregar
 os  e componentes necessarios para executar mecanismo de aprendizagem, como a memoria, o metodo de seleção da ação
 e a aprendizagem
'''
class ControloAprendRef(Controlo):
    def __init__(self):
        self._rmax = 100
        self._rmin = 1
        self._s = None
        self._a = None

        self._mec_aprend = MecAprend([Accao(direccao) for direccao in Direccao])
        ''''''

    def processar(self, percepcao):
        '''return accao'''
        #executar o algoritmo Q-learning

        #vai ser selecionado uma ação para o proximo estado
        sn = EstadoAgente(percepcao.posicao) #observar o proximo estadoagente

        #para aprender é necessario o estado e a ação
        if self._s: #so sprende se houver estado
            r = self.gerar_reforco(percepcao)
            self._mec_aprend.aprender(self._s, self._a, r, sn)
        an = self._mec_aprend.selecionar_accao(sn) #Gerar a açao seguinte
        #atualizar o estado e acao
        self._s = sn
        self._a = an
        self.mostrar()
        return an

    '''Gerar o reforço, da se uma recompensa se  houver recolha de alvo, caso contrario penaliza se'''
    def gerar_reforco(self, percepcao):
        #para gerar um reforço, é porque houve uma acçao, e avera uma recompensa negativa
        r = -self._rmin

        if percepcao.recolha:
            r += self._rmax
        elif percepcao.colisao:
            r -= self._rmax
        return r
        '''return double'''

    def mostrar(self):
        #politica otima para um estado é a acao que maximiza a função Q
        estados = self._mec_aprend.estados
        politica = {s: self._mec_aprend.accao_sofrega(s) for s in estados}
        #valor do q no estado e da ação que maximiza a função q, accao sofrega
        valor = {s: self._mec_aprend.q(s, politica[s]) for s in estados}
        
        self.vista.limpar()
        self.vista.mostrar_valor(valor)
        self.vista.mostrar_politica(politica)