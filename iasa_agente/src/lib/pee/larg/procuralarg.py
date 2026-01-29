from pee.larg.fronteiraFIFO import FronteiraFifo
from pee.mec_proc.procuragrafo import ProcuraGrafo

'''Nesta estratégia de procura, Procura em larguram explora primeiro os nós mais antigos
Ou seja, vai se explorar um nó e depois de concluir que esse não é o objetivo e de colocar os nós seguintes na fronteira, 
a função vai analisar o nó que esta na fronteira à mais tempo, que, caso o nó (referente ao inicio da frase) tenha "irmãos", serão esses.
É como se estivesse a analisar por níveis(degraus) da árvore.

É então usado uma fronteira do tipo First In First Out.
'''
class ProcuraLarg(ProcuraGrafo):
    def iniciar_fronteira(self):
        return FronteiraFifo()