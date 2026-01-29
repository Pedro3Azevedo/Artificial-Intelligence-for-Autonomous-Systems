from abc import ABC, abstractmethod # para indicar que é classe e método absrato, respetivamente

'''
Um estimulo, faz parte de uma reação, este evento é o que vai provocar uma resposta.
Nesta interface, é detetado o estimulo numa perceção, onde atribuirá um nivel de instesidade desse estímulo,
e a partir dessa intensidade, averá um tipo de resposta. Para acontecer essa deteção, é necessário chamar
a função abaixo "dectar", fornecendo a percepcao '''
class Estimulo(ABC):
    @abstractmethod
    def detectar(self, percepcao):
        """Detectar estimulo numa percepcao"""
