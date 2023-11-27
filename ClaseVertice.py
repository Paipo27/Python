

class Vertice:
    def __init__(self,clave):
        self.id=clave
        self.conectadoA={}
    
    def agregarVecino(self,vecino,ponderacion=None):
        self.conectadoA[vecino]=ponderacion

    def __str__(self):
        return str(self.id)+' conectadoA: '+ str([x.id for x in self.conectadoA])
    
    def obtenerConexion(self):
        return self.conectadoA.keys()
    
    def obtenerID(self):
        return self.id
    
    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]