from sae import Accao

from ecr.resposta import Resposta

''' Classe ja implementada na classe Resposta da biblioteca ecr.
    Neste caso a ação de resposta vai ser uma direcao. Por isso,
    no construtor da classe, utiliza-se o construtor super, 
    onde em vez de se fornecer uma accao, atribui se uma direcao 
   '''
class RespostaMover(Resposta):
    def __init__(self, direcao):
        super().__init__(Accao(direcao))
        