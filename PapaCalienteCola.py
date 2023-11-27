from Cola1 import cola

def papaCaliente(listaNombres,N):
    colaSimulacion=cola()
    for nombre in listaNombres:
        colaSimulacion.agregar(nombre)
    
    while colaSimulacion.tamano()>1:
        for i in range (N):
            colaSimulacion.agregar(colaSimulacion.avanzar())
        
        colaSimulacion.avanzar()
    return colaSimulacion.avanzar()
jugadores=["bill","David","Susan","Jane","Kent","Brad"]
print(papaCaliente(jugadores,7))