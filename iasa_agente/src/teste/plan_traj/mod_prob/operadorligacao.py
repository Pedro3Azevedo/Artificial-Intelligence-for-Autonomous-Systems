from mod.operador import Operador
from teste.plan_traj.mod_prob.estadolocalidade import EstadoLocalidade

'''Como referido na classe Operador, um operador representa uma ação quando aplicada, uma transiçãop de estdo.
Neste caso, ao transitar de estado, está se a transitar de localidade.'''
class OperadorLigacao(Operador):
    def __init__(self, origem, destino, custo):
        self._origem = origem
        self._destino = destino
        self._custo = custo
        self._estado_origem = EstadoLocalidade(origem)
        self._estado_destino = EstadoLocalidade(destino)

    '''Ao aplicar o operador ao a um estado, é necessário verificar se o estado a que se esta a aplicar o operador,
    é igual ao estado origem do operador, pois se não for o caso, não é possivel aplicar o operador.'''
    def aplicar(self, estado):
        if estado == self._origem and estado != self._destino:
            return self._estado_destino
        else:
            return None

    def custo(self, estado, estado_suc):
        return self._custo
        