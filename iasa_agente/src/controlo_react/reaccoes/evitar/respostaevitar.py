import random
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae import Direccao

'''Esta classe é a resposta para quando se quer evitar um objeto.
    Nesta classe o objetivo é encontrar uma direção livre, isto é, sem haver um contacto com um objeto.
    Depois ativa se a resposta mover para mover na direção livre
    '''
class RespostaEvitar(RespostaMover):

    def __init__(self, dir_inicial=Direccao.ESTE):
        super().__init__(dir_inicial)
        self._direccoes = list(Direccao)


        '''Nesta função, procura se uma direção livre, com os passos, verificar se há contacto com objeto, 
        precepccionando o contacto com obstaculo na direccao atual, se houver contacto, então procura se um direcao livre
        ,com a função desta class, se houver uma direção livre, altera se a direção da accao para essa e depois
        ativa se a resposta de mover, para essa direccao.
        '''
    def activar(self, percepcao, intensidade):
        if percepcao.contacto_obst(self._accao.direccao):
            direccao_livre = self._direccao_livre(percepcao)
            if direccao_livre != None:
                self._accao.direccao = direccao_livre
                return self.activar(percepcao, intensidade)
            else:
                return None
        else:   
           return super().activar(percepcao, intensidade)
        
    '''Nesta função, é devolvido uma direccao aletória que não tem contacto com obstaculos.
    É criada uma lista de direções livres atraves de um ciclo que vai a cada direção e perceciona se esta em contacto com objeto,
    so coloca na lista se não estiver em contacto.'''
    def _direccao_livre(self, percepcao):
        dir_livre = [direccao for direccao in self._direccoes
                    if not percepcao.contacto_obst(direccao)]
        return random.choice(dir_livre) 