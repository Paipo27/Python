from ClassArbolBinario import ArbolBinario
from FucionesArbol2 import *

libro=ArbolBinario('Libro')
libro.insertarIzquierdo('Seccion 1.1')
libro.insertarIzquierdo('capitulo 1')
libro.insertarDerecho('Seccion 2.2.2')
libro.insertarDerecho('Seccion 2.2')
libro.insertarDerecho('Capitulo 2')
libro.obtenerHijoIzquierdo().insertarDerecho('Seccion 1.2.2')
libro.obtenerHijoDerecho().insertarDerecho('Seccion1.2')
libro.obtenerHijoIzquierdo().obtenerHijoDerecho().insertarIzquierdo('Seccion 1.2.1')
libro.obtenerHijoDerecho().insertarIzquierdo('Seccion 2.1')
libro.obtenerHijoDerecho().obtenerHijoDerecho().insertarIzquierdo('Seccion 2.2.1')

print('Recorrido en en preorden')
preorden(libro)
print('Recorrdio en inorden')
inorder(libro)
print('Recorrido en Postorden')
postorden(libro)