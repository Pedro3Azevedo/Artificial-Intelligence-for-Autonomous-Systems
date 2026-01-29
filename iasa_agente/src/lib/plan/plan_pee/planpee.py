from pee.melhor_prim.informada.procuraaa import ProcuraAA
from pee.melhor_prim.informada.procurasofrega import ProcuraSofrega
from pee.melhor_prim.procuracustounif import ProcuraCustoUnif
from plan.plan_pee.heurdist import HeurDist
from plan.plan_pee.problemaplan import ProblemaPlan
from plan.planeador import Planeador


class PlanPee(Planeador):
    '''No construtor deste planeador, vai se instanciar o mecanismo de procura que se prentende chegar a solução'''
    def __init__(self):
       #self._procura = ProcuraCustoUnif()
       self._procura = ProcuraAA()
       #self._procura = ProcuraSofrega() 
       self._solucao = None

    '''Criar instancia problema, heusristica, resolver, guardar soluçao
        No caso deste planeador, vai se criar o ProblemaPlan, e a HeurDist, 
        a heuristica que calcula a distancia entre o estado e o estado final
        Para concluir, aplica se o resolver do metodo de procura, com o problema e a heuristica fornecida
        que retornara a soluçao
    '''
    def planear(self, modelo_plan, objectivos):
        ''''''
        problema = ProblemaPlan(modelo_plan, objectivos[0])
        heuristica = HeurDist(objectivos[0])
        #self._solucao = self._procura.resolver(problema) #para custo uniforme nao se usa heuristica
        self._solucao = self._procura.resolver(problema, heuristica)

    '''classe para depois executar o passo
        No caso de haver solucao, vai se buscar o proximo passo da mesma para avançar no percurso,
        é dado um passo no percurso, este mesmo é retirado da lista da solução. 
    '''
    def obter_accao(self, estado):
        '''O removerPassso que retira o primeiro passo da solução, utilizando no obter accao'''
        if self._solucao:
            passo = self._solucao.remover_passo() 
            if estado == passo.estado:
                return passo.operador
        return None


    '''Plano existir e o estado inicial corresponde ao estado do agente
        estado atual do agente

        Para o plano ser valido, tem que existir, havendo uma solução para tal, 
        e o estado que o agente se encontra é o mesmo estado do da solução, ou seja
        o estado no percurso onde o agente esta.
    '''
    def plano_valido(self, estado):
        return self._solucao != None and self._solucao[0].estado == estado

    def terminar_plano(self):
        self._solucao = None

    def mostrar(self, vista):
        '''O dicionario estadosCusto, vai buscar os estados explorados que estão armazenados no metodo de procura utilizado
            No metodo de procura, que tem que ser um dos metodos de procura grafo, tem um dicionario que é explorados, este dicionario
            é composto pelo estado de um no e a value é o nó. Por isso, para criar o dicionario estadoCusto, associa se o key dos explorados
            e vai se buscar o custo associado ao no do value do estado do dicionario dos explorados. Neste caso ainda convertemos para negativo para 
            ao fazer o mostrar aparecer a vermelho. 
        '''
        estadosCusto = {a : -(self._procura._explorados.get(a).custo) for a in self._procura._explorados}
       
        '''Tendo o dicionario com o estado como key e a sua value o custo do nó desse estado dos explorados,
        é possivel executar o metodo mostrar_valor do vista. Quanton melhor o custo, ou seja por onde o agente vai percorrer,
         mais intenso fica o vermelho. É executado esta funcao dentro deste metodo pois tem acesso ao metodo de procura, e porque 
         sempre que é processado é executado este metodo, assim apos cada planeamento, depois de reconsiderado. Ou seja, sempre que o agente
         vai para outro alvo, é mostardo o valor dos estados em vermelho. '''
        vista.mostrar_valor(estadosCusto)
        return vista.mostrar_solucao(self._solucao)