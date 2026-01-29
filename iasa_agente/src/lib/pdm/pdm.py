class PDM():
    '''Processo de Decisão de Markov

        Um processo estocástico tem a prioridade de Marvov se
        a distribuição probabilistica condicional dos estados futuros
        de um processo depender exclusivamente do estado presente.
        A previsão dos estados seguintes só depende do estado presente.

        Com este processo podemos resolver o problema de decisao ao longo do tempo,
        a utilidade de uma ação vai depender de uma sequencia de decisões , que tera 
        possibilidade de ganho e de perdas. 

        

    '''


    '''Gama pode variar ente 0 e 1, é um fator de tempo de oportunidade, Fator de desconto, quanto maior o valor, 
    conseguese ver melhor o futuro, baixando o gama, esta se a operar no presente'''
    def __init__(self, modelo, gama, delta_max):
        self._modelo = modelo
        self._gama = gama
        self._delta_max = delta_max

    '''calcula a utilidade de todas as acoes, efeito cumulativo da
    evolução da situação. ganho ou perda num determinado estado, 
    tera um falor finito ou infinito.
    
    Utilidade = reconpensa associada ao estado + (gama * a Utilidade do estado seguinte)
    podemos ver esta expressao na pagina 15 do documento Processos de Decisão sequencial
    '''
    def utilidade(self):
        '''Return Utilidade'''
        A, S = self._modelo.A, self._modelo.S 
        #associa um estado a um valor que é o efeito cumulaticvo das recompensas
        U = {s: 0 for s in S()}

        while True:
            
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([self.util_accao(s, a, U) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))
                #transformar numa lista ao colocar default, e tem que se colocar o default pois A(s) o«pode ser vazio
           
            #quanto maior o gama, melhor sera a solução, pois foi se mais ao futuro, porem que
            #requer muitas iterações, muito tempo.
            # Chega a uma altura que vemos um padrao e que a diferença entre a probabilidade dos estados
            # é sempre semelhante, podendo deduzir logo qual o estado com maior probabilidade.
            if delta <= self._delta_max:
                break
        return U

    '''Calcula a utilidade de uma ação especifica
        Somatorio(s') T(s,a,s')[R(s,a,s')+gamaU(s')] para todo s pertencente a S
                           |
                           v
                        separar o s' e adicionar a probabilidade
                        daddo o estado e a ação, 
                         fornece uma lista de trancisao com probabilidade e estado seguinte         
    
    '''
    '''s-Estado, a-Operador, U-Utilidade'''
    def util_accao(self, s, a, U):
        '''Return double'''
        T, R, gama = self._modelo.T, self._modelo.R, self._gama
        return sum(p * (R(s, a, sn) + gama*U[sn]) for p, sn in T(s, a))
    


    '''Forma de representação do comportamento do agente,
    define qual a accao que deve ser realizada em cada estado, a estrategia de accao
    
    Existe a Politica determinista e a não determinista
    
    Para calcular a politica verifica se para cada s qual a acao com o valor maximo,
    politica do estado = argmax (da utilidade)
    verifica se esta expressao na pagina 15 do documento Processos de Decisão sequencial
    '''
    def politica(self, U):
        '''Return Politica'''
       
        A, S = self._modelo.A, self._modelo.S
        pol = {}
        
        #associa um estado a uma açao
        for s in S():
            if len(A(s)) != 0:
                pol[s] = max(A(s), key=lambda a : self.util_accao(s, a, U))
                #devolve a acao de A(s) com o valor máximo
        return pol


    #devolve a Utilidade e a politica
    #Resolve a deciao de Markov, de acordo com o modelo dado
    def resolver(self):
        '''Return Tuple<Utilidade, Politica>'''
        U = self.utilidade()
        pol = self.politica(U) #politica da utilidade resolvida em cima
        return U, pol

