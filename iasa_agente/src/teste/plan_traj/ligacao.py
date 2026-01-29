from dataclasses import dataclass
import string
'''Dataclass que representa uma ligação entre dois pontos tendo armazenado o local de origem e o local de destino, assim como o seu custo'''
@dataclass
class Ligacao:
    origem : string
    destino : string
    custo : int
