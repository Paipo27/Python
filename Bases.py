

from ProgaramaPila import Pila 

def dividirPor2 (numeroDecimal):
    pilasResiduo=Pila()
    
    while numeroDecimal > 0:
        residuo=numeroDecimal % 2
        pilasResiduo.incluir(residuo)
        numeroDecimal=numeroDecimal//2
        
    cadenaBinaria=""
    
    while not pilasResiduo.estaVacia():
            cadenaBinaria=cadenaBinaria + str(pilasResiduo.extraer())
            
    return cadenaBinaria
