from controlo_react.controloreact import ControloReact
from controlo_react.reaccoes.recolher import Recolher
from sae.simulador import Simulador


#Ativaçao
controlo = ControloReact(Recolher())
Simulador(1, controlo).executar()