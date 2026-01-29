from pee.prof.procuraproflim import ProcuraProfLim

'''Neste método de procura é realizado com as mesmas regras que a sua superclasse, Procura por Profundidade limitada, 
mas vai tentar resolver o problema limitando a profundidade, com a particularidade de ir aumentando o nivel máximo da profundidade'''
class ProcuraProfIter(ProcuraProfLim):
    def resolver(self, problema, inc_prof=1, prof_max=1000):
        ip = inc_prof
        for ip in range(prof_max):
            solucao = super().resolver(problema, ip)
            if solucao:
                return solucao
