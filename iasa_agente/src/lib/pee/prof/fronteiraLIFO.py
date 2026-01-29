from pee.mec_proc.fronteira.fronteira import Fronteira

'''Este tipo de fronteira funciona em Last in First Out,
ou seja, o ultimo nó a ser adicionado, será o primeiro a ser removido.
Para tal, é usado o método insert() com o index a 0. '''
class FronteiraLifo(Fronteira):
    def inserir(self, no):
        self._nos.insert(0, no)