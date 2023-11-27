

def preorden(arbol):
        if arbol:
            print(arbol.obtenerValorRaiz())
            preorden(arbol.obtenerHijoIzquierdo())
            preorden(arbol.obtenerHijoDerecho())

def postorden(arbol):
      if arbol!=None:
            postorden(arbol.obtenerHijoIzquierdo())
            postorden(arbol.obtenerHijoDerecho())
            print(arbol.obtenerHijoDerecho())

def inorder(arbol):
      if arbol!=None:
            inorder(arbol.obtenerHijoIzquierdo())
            print(arbol.obtenerHijoDerecho())
            inorder(arbol.obtenerHijoDerecho())
           