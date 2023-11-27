from ClassArbolBinario import ArbolBinario
from FucionesArbol2 import *

Universidad=ArbolBinario('Universidad')
Universidad.insertarIzquierdo('Electrica')
Universidad.insertarIzquierdo('Minas')
Universidad.insertarIzquierdo('Medellin')
Universidad.insertarDerecho('Industrial')
Universidad.insertarDerecho('Ingenieria')
Universidad.insertarDerecho('Manizales')
Universidad.obtenerHijoIzquierdo().obtenerHijoIzquierdo().insertarDerecho('Sistemas')
Universidad.obtenerHijoIzquierdo().insertarDerecho('Ciencias')
Universidad.obtenerHijoDerecho().insertarIzquierdo('Administracion')
Universidad.obtenerHijoDerecho().obtenerHijoIzquierdo().insertarIzquierdo('informatica')
Universidad.obtenerHijoDerecho().obtenerHijoIzquierdo().insertarDerecho('Empresas')
Universidad.obtenerHijoDerecho().obtenerHijoDerecho().insertarIzquierdo('Civil')

print('Recorrido en preorden')
preorden(Universidad)
print('Recorrido en inorden')
inorder((Universidad))
print('Recorrido en postorden')
inorder(Universidad)