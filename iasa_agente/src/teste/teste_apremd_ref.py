

from controlo_aprend.controloaprendref import ControloAprendRef
from sae import Simulador

#Ativaçao
controlo = ControloAprendRef()
Simulador(2, controlo, reiniciar=True).executar()