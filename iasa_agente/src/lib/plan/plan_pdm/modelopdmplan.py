from pdm.modelopdm import ModeloPDM
from plan.modeloplan import ModeloPlan


'''Ao implementar a classe ModeloPlan e ter como um atributo um modelo_plan que implementa ModeloPlan
    conseguimos reutilizar codigo, para pudermos usar este planeador no ControloDeliberativo, sem ter que
    alterar código nesse, fica compativel com o Planeador. Tem que ganrantir o contracto ModeloPDM pois 
    este modelo é de Processo de Decisão de Marcov. 
    Por isso delega se os metodos estado(), estados(), operadores() à instancia de modelo_plan 

    
'''
class ModeloPDMPLan(ModeloPDM, ModeloPlan):
    def __init__(self, modelo_plan, objectivos):
        self._modelo_plan = modelo_plan
        self._objectivos = objectivos
        self._rmax = 1000 #valor de recompensa maxima para valorizar objetivos

    def estado(self):
        '''return Estado'''
        return self._modelo_plan.estado()
    
    def estados(self):
        '''return List<Estados> '''
        return self._modelo_plan.estados()

    def operadores(self):
        '''return List<Operadores>'''
        return self._modelo_plan.operadores()

    '''Os métodos tem que estar presentes mesmo sabendo que estes são iguais aos métodos acima,
    pois é necessário garantir a compatibilidade com os metodos de Decisao de Marcov'''
    def S(self):
        '''return List<Estados>'''
        return self.estados()

    '''Se o estado for terminar, retorna vazio, nao tem operadores, se não for
    estado terminal, retorna os operadores desponiveis'''
    def A(self, s):
        '''Return List<Operadores> '''
        if s in self._objectivos:
            return list()
        return self.operadores()


    def T(self, s, a):
        '''return list<Transicao>'''
        '''aplica se o operador ao estado para obter o estado seguinte e caso este exista retorna
        uma lista da transição para o estado seguinte com a probabilidade de 100% pois é um modelo determinista'''
        sn = a.aplicar(s)
        if sn:
            return [(1, sn)]
        return list()

    '''Reconpensa esperada na transição do estado para o estado seguinte apartir da aplicação da açao'''
    def R(self, s, a, sn):
        '''return double'''
        '''Se atingirmos o objetivo a recompensa sera a recompensa maxima'''
        recompensa = a.custo(s, sn) * (-1) #valor negativo
        if sn in self._objectivos:
            return self._rmax + recompensa
        return recompensa
        
