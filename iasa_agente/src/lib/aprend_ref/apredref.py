from abc import abstractclassmethod

'''Aprendizagem por Reforço

Esta aprendizagemé apartir da interaccao com o ambiente. 
Aqui é tem se em consideração o Estado, a ação e o reforço, que é o ganho ou a perda.
Esta aprendizagem é uma aprendizagem comportamental, fazemos a pergunta O que fazer?
Que comportamento executar, que ação executar?
'''
class ApredRef():
    def __init__(self, mem_aprend, sel_accao):
        self.mem_aprend = mem_aprend
        self.sel_accao = sel_accao

    '''Este método é o método onde o agente aprende, vai explorar e vai
        aprender qual o reforço do estado e da ação , atualiza o Q

        É aplicado um algoritmo.
    '''
    @abstractclassmethod
    def aprender(self, s, a, r, sn):
        '''s- Estado, a - Accao, r- Reforço, sn - EstadoSeguinte'''