import math
from controlo_delib.modelomundo import ModeloMundo
from sae import Controlo
from sae.ambiente.elemento import Elemento

'''O controlo Deliberado é constituida por uma  arquitetura de agentes deliberativos.
Nesta arquitetura existe uma ambiente e um agente, o agente contém memoria, e depois de
uma percepcao, ao processar, vai se assimilar a percepçao, e de seguida existe uma deliberação, 
ou seja, o ambiente pode ter alterações, e com isso a ação pode ser diferente, por isso
 vai se reconsiderar antes de executar, e caso haja uma alteração no ambiente, delibera se:
 Vai se decidir o que fazer, vendo as opções, produzindo uma lista de objetivos. De seguida 
 tem que se planear, decidir como o fazer, que ações executar, o que faz com se forme planos.
 
 Em suma, o Processo geral de tomada de decisão,  vai se observar o mundo, atualizando o seu modelo,
 depois deliera se o que fazer, planeando como o fazer e executando o plano de acçao.

 Um Problema deste raciocinio, é que existem recursos computacionais limitados, tal como a memoria e o 
 tempo de ccomputação. Para alem disso, o Ambiente pode mudar durante o raciocinio, 
 e com isso, o resultado pode nao ser consistente.


 Esta classe vai conter um planeador, um ModeloMundo e os objetivos.
 '''
class ControloDelib(Controlo):
    def __init__(self, planeador):
        self._planeador = planeador
        self._modelo_mundo = ModeloMundo()
        self._objectivos = []

    '''
    Ao processar, vai assimilar a percepcao e depois vai reconsiderar,
     pois, caso haja alterações tem que se alterar o plano, então delibera se
     e de seguida planei a se e depois executa se. Caso não haja alteração, 
     não é preciso reconsiderar então executa se o plano. 
    Return Accao'''
    def processar(self, percepcao):
        
        self.assimilar(percepcao)
        if self.reconsiderar():
            self.deliberar()
            self.planear()
        self.mostrar()
        return self.executar()
        

    '''incorporar a informaçao da percepçao no modelo do mundo, atualizando, 
    pois o método atualizar, verifica se os elementos percepcionados estão presentes no modelo mundo
    '''
    def assimilar(self, percepcao):
        self._modelo_mundo.actualizar(percepcao)

    '''
    Caso haja alteração no modelo do mundo, ent~~ao tem que se reconsiderar, logo return true
    Se o plano já nao for valido, tambem tem que se reconsiderar, pois o agente pode já não estar no estado certo,
    ou pode ja não haver uma solucao, ou plano
    return Boolean'''
    def reconsiderar(self):
        return self._modelo_mundo.alterado or not self._planeador.plano_valido(self._modelo_mundo.estado())

    '''
        Atualizar o conjunto de objetivos. O agente tem como função 
        recolher todos os alvos. Para atualizar, é necessario verificacr as opções,
        Por isso, tem que se ver no Modelo do Mundo os elementos que são alvos.
        Ou seja os objetivos vao ser uma lista de estados que pertencem aos estados 
        do modelo do mundo cujo elemento na posiçao desses estados sejam um alvo.
        Organiza se os objetivos de forma a que estes esjam por oredem de mais  perto do estado atual
        void'''
    def deliberar(self):
        self._objectivos = [estado 
                            for estado in self._modelo_mundo.estados()
                            if self._modelo_mundo.obter_elem(estado) == Elemento.ALVO]
        if self._objectivos:
            estado_atual = self._modelo_mundo.estado()
            self._objectivos.sort( key=lambda estado : math.dist(estado.posicao, estado_atual.posicao))
  
    
    #    A partir dos objetivos e do modelo do mundo, pode se fazer um plano, planear,
     #   mas no caso de não haver objetivos, é necessário terminar algum plano que esteja a executar.
      #  Pois podemos ter um plano e o ambiente alterar, ficando sem objetivos, ai o plano já não é nececssario
    
    def planear(self):
        if self._objectivos:
            self._planeador.planear(self._modelo_mundo, self._objectivos)
        else:
            self._planeador.terminar_plano()

    '''
    Para exxecutar, é necessario ir obter a ação do planeador do estado atual, 
    o metodo presente só obtem o operador, logo, caso haja um operador, retorna se a ação do operador.

    O que acontece neste método é que vai e obter o proximo passo da solução, para percurrer o percusro ate ao destino final,
    Com a funçao obter_acao tem se o operador do passo do percurso que se percorre, e com esse operador obte, se a acao
    para se avançar
 '''
    def executar(self):
        operador =  self._planeador.obter_accao(self._modelo_mundo.estado()) 
        if operador == None:
            return None
        
        return operador.accao
        

    '''void'''
    def mostrar(self):
        self.vista.limpar()
        self._modelo_mundo.mostrar(self.vista)
        self._planeador.mostrar(self.vista)
        self.vista.mostrar_estados(self._objectivos)

       
    
'''apresentar o custo representado a vermelho
    mostrar_valor(dict<estado, valor>)
'''