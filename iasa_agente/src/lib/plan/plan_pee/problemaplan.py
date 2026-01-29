from mod.problema.problema import Problema

class ProblemaPlan(Problema):
    '''O problema é constiuido pelo estado atual onde o agente se encontra no espaço, no modelo mundo,
    e pelos operadores do plano.'''
    def __init__(self, modelo_plan, estado_final):
        self._estado_final = estado_final
        super().__init__(modelo_plan.estado(), modelo_plan.operadores())

    '''Objetivo é o agente chegar ao estado final'''
    def objectivo(self, estado):
        return estado == self._estado_final