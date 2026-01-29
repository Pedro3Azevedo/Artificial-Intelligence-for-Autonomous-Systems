from aprend_ref.memoriaaprend import MemoriaAprend

'''A memoria esparsa, é um tipo de memoria que vai guardar os estados e ações,
e associa los ao valor Q

Com esta memoria, minimiza o numero de entradas, fornece só as estradas necessarias
Contudo tem os estados e ações todos, mas com o valor de omissão. Ilude o facto de haver
muita informação, permitindo exxecutar a função
'''
class MemoriaEsparsa(MemoriaAprend):
    def __init__(self, valor_omissao = 0):
        #valor dado para os estados e ações que ainda não foram explorados
        self._valor_omissao = valor_omissao
        self._estados = set()
        #É usado um dicionario assossiando um tuplo com o estado e a acao e o valor correspondendo ao Q
        self._memoria = dict()

    @property
    def memoria(self):
        return self._memoria

    #Ir ao dicionario e ir buscar o valor do Q do estado e da ação
    def q(self, s, a):
        return self._memoria.get((s, a), self._valor_omissao)

    '''atualizar a memoria, associar ao estado accao o valor q e depois adicionar o estao a lista de estados'''
    def atualizar(self, s, a, q):
        self._memoria[(s, a)] = q
        self._estados.add(s)

    def obter_estados(self):
        return self._estados
