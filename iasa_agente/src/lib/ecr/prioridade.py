from .comportcomp import ComportComp
from sae import Accao

'''
    As Acções da biblioteca sae, contêm uma prioridade associda.
    As respostas são selecionadas de acordo com uma prioridade associada
    que varia ao longo da execução.
    Quanto maior o numero associado á prioridade, mais importante é a ação.
    Nesta forma de selecionar acçao, é escolhida a accao com maior prioridade
'''
class Prioridade(ComportComp):
    '''Nesta função, caso haja accoes, vai se returnar a accao cuja a prioridade seja maior,
    para isto, é usada a função max (que devolve o elemento que tenha o atributo maior),
    e é usada uma função anónima (lambda) que indicará que o atributo maior que se pretende
    comparar é a prioridade.'''
    def selecionar_accao(self, accoes):
        if accoes:
            return max(accoes, key=lambda accao: accao.prioridade)
        


