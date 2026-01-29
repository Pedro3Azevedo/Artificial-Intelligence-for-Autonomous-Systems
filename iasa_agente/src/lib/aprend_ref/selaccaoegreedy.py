import random
from aprend_ref.selaccao import SelAccao

'''
Para resolver o Dilema Explorar ou aproveitar, temos que responder a pergunta
Quando é que se aprendeu o suficiente para começar a aplicar o que se aprendeu?

Quando se começa a procurar, ainda não se conhece o espaço, logo tem que se explorar
primeiro, e ao longo do tempo começa se a aproveitar o que já se aprendeu.
Para tal, usamos a Seleção de ação Epsilon Greedy.

A selecao Epsilon Greedy, é uma forma que, dependendo do valor do epsilon,
 vai tando explorar, como selecionar a acao que maximiza o valor do estado-accao ,
  o valor Q
  
O Epsilon vai ser um valor entre 0 e 1, onde define a probabilidade de executar cada 
ação. Quanto maior o valor do epsilon, mais provavel é o agente de ir explorar, mas quanto menor,
mais usa o que aprendeu e escolhe a ação que faz com que haja um amior valor de Q.
  
  '''

class SelAccaoEGreedy(SelAccao):
    def __init__(self,mem_aprend, accoes, epsilon):
        #determina a propabilidade de exploração
        self._epsilon = epsilon
        #contem uma memoria de aprendizagem 
        self._mem_aprend = mem_aprend
        #lista de accoes
        self._accoes = accoes

    '''método que define qual o tipo de seleção'''
    def seleccionar_accao(self, s):
        #caso o valor random seja maior que o valor do epsilon, aplica se a ação sofrega
        if random.random() > self._epsilon:
            return self.accao_sofrega(s)
        #caso seja menor que o epsilon , o agente vai explorar, logo, fazer uma escolha aleatoria
        else:
            return self.explorar()
        '''return accao'''

    '''Vai devolver a ação que, no momento, maximiza o valor de q'''
    def accao_sofrega(self, s):
        '''return accao'''

        #para o caso de accoes terem o mesmo valor, a função abaixo vai retornar sempre a primeira,
        #evitando a fazer accoes com o mesmo valor, por isso executa se uma baralhar das accoes
        random.shuffle(self._accoes)
        #a* = argmax(a in accoes, Q(s, a))
        return max(self._accoes, key=lambda a: self._mem_aprend.q(s, a))

    '''vai devolver uma accao explorada
        uma accao aleatoria.
    '''
    def explorar(self):
        return random.choice(self._accoes) #executa um choice de uma ação do conjunto de ações que existem
        '''return accao'''