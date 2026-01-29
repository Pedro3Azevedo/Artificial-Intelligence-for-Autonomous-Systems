from controlo_delib.controlodelib import ControloDelib
from plan.plan_pee.planpee import PlanPee

from sae import Simulador
planeador = PlanPee()
#Ativaçao
controlo = ControloDelib(planeador)
Simulador(4, controlo).executar()