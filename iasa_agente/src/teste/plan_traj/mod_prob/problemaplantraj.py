from mod.problema.problema import Problema
from teste.plan_traj.mod_prob.estadolocalidade import EstadoLocalidade
from teste.plan_traj.mod_prob.operadorligacao import OperadorLigacao

'''Este problema consiste num conjunto de localidades ligadas entre si,(uma localidade pode não estar ligada a todas as outras localidades)
Um operador é representado por uma ligação, pois ambos têm um estado/localidade de origem e um de destino também como um custo.
 O objetivo do problema é, apartir de um estado localidade, planear um trajeto (a partir de um mecanismo de procura) até a um determinado estado de destino.
 Ao criar este problema, é criado os EstadoLocalidade inicial e final, e com o conjunto de ligações recebidas, criar os OperadorLigação.
  '''

class ProblemaPlanTraj(Problema):
    def __init__(self, ligacoes, loc_inicial, loc_final):
        self._estadoInicial = EstadoLocalidade(loc_inicial)
        self._estadoFinal = EstadoLocalidade(loc_final)

        operadores = list()
        for ligacao in ligacoes:
            operadores.append(OperadorLigacao(ligacao.origem, ligacao.destino, ligacao.custo ))
       
        super().__init__(self._estadoInicial, operadores)
        self._ligacoes = ligacoes
        self._loc_inicial = loc_inicial
        self._loc_final = loc_final

    '''Como referido anteriormente, só se chega ao objetivo, quando o estado for igual ao estadoFinal, o estadoLocalidade de destino'''
    def objectivo(self, estado):
        return estado == self._estadoFinal
        
