'''Utilizar o ambiente 3'''
from controlo_delib.controlodelib import ControloDelib
from plan.plan_pdm.planpdm import PlanPDM


from sae import Simulador
planeador = PlanPDM()
#Ativaçao
controlo = ControloDelib(planeador)
Simulador(3, controlo).executar()