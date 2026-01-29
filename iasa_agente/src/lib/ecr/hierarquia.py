from .comportcomp import ComportComp

''' Os comportamentos estão organizados numa hierarquia fixa de supressão
    Nesta forma de seleção de ação, ha uma ordem fixa, com isto,
     os comportamentos ja estão ordenados por ordem de prioridade.
     Logo, a acção a ser selecionada, é a primeira da lista.
     Mais prioridade, indice mais baixo.
'''
class Hierarquia(ComportComp):
    def selecionar_accao(self, accoes):
        if accoes:
            return accoes[0]