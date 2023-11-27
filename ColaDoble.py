
class ColaDoble1:
    def __init__(self):
        self.items=[]

    def estaVacia(self):
        return self.items==[]
    
    def agregarFrente(self,item):
        self.items.append(item)

    def agregarFinal(self,item):
        self.items.insert(0,item)

    def removerFrente(self):
        return self.items.pop()
    
    def removerfinal(self):
        return self.items.pop()
    
    def tamano (self):
        return len(self.items)
    
    def inspeccionarFinal(self):
        return self.items[len(self.items)-1]
    
    def inspeccionarFrente(self):
        return self.items[len(self.items)-1]