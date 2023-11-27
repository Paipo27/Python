import operator

def evaluar(arbolAnalisis):
 operadores={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
 hijoIzq=arbolAnalisis.obtenerHijoIzquierdo()
 hijoDere=arbolAnalisis.obtenerHijoDerecho()
 if hijoIzq and hijoDere:
        fn=operadores[arbolAnalisis.obtenerValorRaiz()]
        return fn(evaluar(hijoIzq),evaluar(hijoDere))
 else:
        return arbolAnalisis.obtenerValorRaiz()