from pee.larg.procuralarg import ProcuraLarg
from pee.melhor_prim.informada.procuraaa import ProcuraAA
from pee.melhor_prim.informada.procurasofrega import ProcuraSofrega
from pee.melhor_prim.procuracustounif import ProcuraCustoUnif

from pee.prof.procuraprof import ProcuraProf
from pee.prof.procuraprofiter import ProcuraProfIter
from pee.prof.procuraproflim import ProcuraProfLim
from teste.plan_traj.mod_prob.problemaplantraj import ProblemaPlanTraj

'''Classe que vai criar o problema e resolve-lo com um mecanismo de procura, pois,k neste caso, o problema é planear um trajeto de uma localidade a outra.'''


class PlaneadorTrajecto():

    '''Para planear o trajeto, é necessário saber se todas as ligações, a localidade inicial e a final que será o objetivo.
    Apos criado o problema, é escolhido a forma como se quer resolver. Aqui foi criado um conjunto de condições onde que estiver a usar pode escolher o mecanismo de procura.
    Ao ter o problema e um mecanimo de procura só falta resolver, então é chamado o método resolver, obtendo uma solução.
    '''

    def planear(self, ligacoes, loc_inicial, loc_final):
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        self._procura = None
        print("Selecione o mecanismo de procura: ")
        print("0-Procura Profundidade\n1-Procura Profundidade Limitada\n2-Procura Profundidade Iterada\n3-Procura Largura\n4-Procura Custo Uniforme")
        p = input()
        print(p)

        s = ""
        if p == "0":
            self._procura = ProcuraProf()
            s = "Procura Profundidade"
        if p == "1":
            self._procura = ProcuraProfLim()
            s = "Procura Profundidade Limitada"
        elif p == "2":
            self._procura = ProcuraProfIter()
            s = "Procura Profundidade Iterada"
        elif p == "3":
            self._procura = ProcuraLarg()
            s = "Procura Largura"
        elif p == "4":
            self._procura = ProcuraCustoUnif()
            s = "Procura Custo Uniforme"
        '''elif p == "5":
            self._procura = ProcuraAA()
            s = "Procura A*"
       elif p == "6":
            self._procura = ProcuraSofrega()
            s = "Procura Sofrega"'''

        print("Calcular caminho da localidade", loc_inicial,
              "a", loc_final, ", com o método de ", s)
        print()
       # if(p<4):
        solucao = self._procura.resolver(problema)
        '''else:
           solucao = procura.resolver(problema, )'''

        return solucao

    '''Método que, caso haja uma solução é mostrada. Como a classe solução terá uma lista com o percurso planeado, e contem uma função __iter__
    que itera os elementos da lista do percurso, basta fazer o ciclo a baixo.'''

    def mostrar_trajecto(self, solucao):
        if(solucao ):
            custo = 0
            for no in solucao:
                print(no.estado.localidade)
                custo = no.custo
            print()
            print("Custo: ", custo)

            '''Para verificar a complexidade dos métodos podemos verificar duas informacoes:
                Complexidade Temporal: que é o número de nós processados, ou seja, o numero de nós que foram expandidos
                Complexidade Espacial: que é o número de nós em memória, ou seja, os nós que permaneceram na fronteira, 
                    no caso do mecanismo de procura por profundidae, e para os mecanismos de procura em grafo, 
                    será o numero de nós que foram explorados.
            '''
            print("Nos processados: ", self._procura._nosProcessados)
            print("Memorizados: ", self._procura._nosEmMemoria)
        else:
            print("Nenhuma solução encontrada...")

            '''
            Problema
            Loc-0 -> Loc-4                  Processados     Memorizados
            Procura Profundidade                3                 3
            Procura Profundidade Limitada       3                 3
            Procura Profundidade Iterada       10                 4
            Procura Largura                     6                 9
            Procura Custo Uniforme             13                 11
           
       
            
            
            '''