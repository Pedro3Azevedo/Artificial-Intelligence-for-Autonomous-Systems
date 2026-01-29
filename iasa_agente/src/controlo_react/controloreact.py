from sae import Controlo

'''
Classe composta por comportamentos, que vai processar perceções e
 ativar a ação desses comportamentos, para de seguida, atuar.
 Este controlo, consicte em haver um agente percecionar, 
 depois, este controlo reativo, vai processar a perceção, 
 ativando o comportamento, forncendo uma ação.
'''
class ControloReact(Controlo):
    def __init__(self, comportamento):
        self.comportamento = comportamento
        self.mostrar_per_dir = True #Mostar o que o agente esta a percepcionar
    
    '''Nesta função, vai se processar a percepcao. 
    Para isto, como a classe Comportamento tem uma funcao ativar que recebe uma perceçao
    e retorna uma ação, nesta função vai se ativar a ação do comportamento.'''
    def processar(self, percepcao):
        return self.comportamento.activar(percepcao)