from pdm.pdm import PDM
from plan.plan_pdm.modelopdmplan import ModeloPDMPLan
from plan.planeador import Planeador



class PlanPDM(Planeador):
    
    def __init__(self):
        '''O valor gama representa uma taxa de desconto para as recompensas diferidas no tempo.
        Quanto maio o valor do gama, é explorado mais no futuro, sendo o ideal verificar o mais para o futuro possivel.
        O valor tem que ser abaixo de 1.
        Este desconto é feito qunado se esta a calcular a utilidade de uma ação onde, ao valor da untilidade
        do estado seguinte é aplicado esse desconto. 
        Pelos testes, quando colocamos um gama mais baixo, o valor da utilidade vai baixando para cada ação,
        e quandoo se tem estados onde a utilidade é negativa, o agente prefere ficar parado, pois fica a perder. 
        
        '''
        
        self._gama = 0.9 
        self._delta_max = 1 #menor variação possivel do valor 
        self._utilidade = None
        self._politica = None

    '''Para pplanear , é necessario criar um modelo PDM onde este terá o Modelo do Mundo e os objetivos,
        Podemos depois criar o Processo de Decisão de Marcov, utilizando o modelo criado, mais o valor do gama e delta maximo.
        Por fim, para obtermos a utilidade e a politica utiliza se o método resolver do PDM. 
        Com isto obetemos os valores de Utilidade e Politica de cada estado, 
        sendo que a utilidade é um dicionario pnde se associa um valor a um estado e a politica 
        um dicionario que associa o estado a uma ação.
        A politica comportamental baseia se na froma de representação do comportamento do agente, 
        define qual a ação que este deve realizar em cada estado. 
        A utilidade vai ter um valor comulativo de estado para estado, com influencia do gama, e o agente
        vai pelo caminho mais benefico, com uma melhor recompensa, pois claro se o caminho for negativo, mais 
        vale ficar parado.
    '''
    def planear(self, modelo_plan, objectivos):
        modelo_pdm = ModeloPDMPLan(modelo_plan, objectivos)
        pdm = PDM(modelo_pdm, self._gama, self._delta_max)
        self._utilidade, self._politica = pdm.resolver()

    #A politica é um dicionario que para cada estado associa uma ação
    def obter_accao(self, estado):
        '''retunr Operador'''
        if self._politica:
            return self._politica[estado]
        return None

    '''Um plano só pode ser válido com uma politica, pois é tambem esta que define para onde o agente avança
    O plano so é valido se o estado pertencer ao mesmo, pertencer a politica.'''
    def plano_valido(self, estado):
        '''return boolean'''
        if self._politica and self._politica[estado]:
            return True
        return False


    def terminar_plano(self):
        '''void'''
        self._politica = None
        self._utilidade = None

    '''O valor da utilidade vai ser representada numa escala de verdes, sendo que quanto maior,
    mais claro e mais verde fica. Quando o valor é negativo, a utilidade é representada numa escala de vermelho,
    quanto menor o valor, mais vermelho fica'''
    def mostrar(self, vista):
        '''void'''
        if self._politica and self._utilidade:
            vista.mostrar_valor(self._utilidade)
            vista.mostrar_politica(self._politica)