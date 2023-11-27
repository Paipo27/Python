import random
from ImpresoraCola import impresora
from Cola1 import cola
from RandomCola import Tarea

def simulacion(numeroSegundos,paginaPorMinuto):
    impresoraLaboratorio=impresora(paginaPorMinuto)
    colaimpresion=cola()
    tiemposEspera=[]

    for segundoActual in range(numeroSegundos):

        if nuevaTareaImpresion():
            tarea=Tarea(segundoActual)
            colaimpresion.agregar(tarea)

        if(not impresoraLaboratorio.ocuapda())and\
                (not colaimpresion.estaVacio()):
            tareaSiguiente=colaimpresion.avanzar()
            tiemposEspera.append(tareaSiguiente.tiempoEspera(segundoActual))
            impresoraLaboratorio.iniciarNueva(tareaSiguiente)

        impresoraLaboratorio.tictac()
    esperaPromedio=sum(tiemposEspera)/float(len(tiemposEspera))
    print("Tiempo de espera promedio %6.2f segundos %3d tareas restantes."\
          %(esperaPromedio,colaimpresion.tamano()))
def nuevaTareaImpresion():
  numero=random.randrange(1,181)
  if numero==180:
    return True
  else:
   return False
for i in range(10):
  simulacion(3600,5)