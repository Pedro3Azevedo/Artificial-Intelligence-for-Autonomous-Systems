from mod.estado import Estado

'''Esta localidade é um tipo de estado, ou seja implementa a classe Estado.
O Estado localidade representa uma localidade, um nó que tenha um EstadoLocalidade, terá uma localidade associada.
E como todos os tipos de estados, cada estado tera um id.'''
class EstadoLocalidade(Estado):
    def __init__(self, localidade):
        self._localidade = localidade
        self._id_valor = self.id_valor()

    def id_valor(self):
        return hash(self.localidade)
        
    @property
    def localidade(self):
        return self._localidade

    