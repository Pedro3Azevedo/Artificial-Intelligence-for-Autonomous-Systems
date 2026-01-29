from pee.mec_proc.fronteira.fronteira import Fronteira

'''Nesta tipo de fronteira , o primeiro nó a ser inserido será o primeiro a ser removido,
First in First out
Para tal é usado a função append que adiciona o nó no final da lista.'''
class FronteiraFifo(Fronteira):
    
    def inserir(self, no):
        self._nos.append(no)