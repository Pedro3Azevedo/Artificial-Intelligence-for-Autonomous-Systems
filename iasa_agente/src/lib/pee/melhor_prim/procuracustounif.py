from pee.melhor_prim.aval.avalcustounif import AvalCustoUnif
from pee.melhor_prim.procuramelhorprim import ProcuraMelhorPrim

'''nesta classe é usado o Avalidaor de custo uniforme, onde a estratégia de controlo é explorar primerio caminhos com menor custo'''
class ProcuraCustoUnif(ProcuraMelhorPrim):
    def iniciar_avaliador(self):
        return AvalCustoUnif()
