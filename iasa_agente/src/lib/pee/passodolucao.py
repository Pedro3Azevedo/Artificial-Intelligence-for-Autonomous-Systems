from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

'''Detalhes do estado e do operador de um passo do percurso da soluçao'''
@dataclass 
class PassoSolucao():
    estado: Estado
    operador: Operador