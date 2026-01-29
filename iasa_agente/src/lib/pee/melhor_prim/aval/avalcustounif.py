from pee.mec_proc.fronteira.avaliador import Avaliador


class AvalCustoUnif(Avaliador):
    def prioridade(self, no):
        return no.custo
