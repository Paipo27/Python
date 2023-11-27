class cola:
    
    
    def __init__(self):
        self.items=[]

    def estaVacio(self):
        return self.items==[]
    
    def agregar(self, item):
        self.items.insert(0,item)
    
    def avanzar(self):
        return self.items.pop()
    
    def tamano (self):
        return len(self.items)