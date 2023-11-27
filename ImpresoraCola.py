
class impresora:
    def __init__(self,pagina):
        self.tasapagina=pagina
        self.tareaActual=None
        self.tiempoRestante=0

    def tictac(self):
        if self.tareaActual!=None:
            self.tiempoRestante=self.tiempoRestante-1
            if self.tiempoRestante==0:
                self.tareaActual
    
    def ocuapda(self):
        if self.tareaActual!=None:
            return True
        else:
            return False
    def iniciarNueva(self,nuevaTarea):
        self.tareaActual=nuevaTarea
        self.tiempoRestante=nuevaTarea.obtenerPagina()*60/self.tasapagina