from sae import Controlo
from sae import Simulador

class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("processar")

#Ativaçao
controlo = ControloTeste()
Simulador(1, controlo).executar()