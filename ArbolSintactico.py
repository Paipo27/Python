from ClassArbolBinario import ArbolBinario
from ProgaramaPila import Pila
from FucionesArbol2 import *

def construirArbolAnalisis(expresionAgrupada):
    listaSimbolos = expresionAgrupada.split()
    pilaPadres = Pila()
    arbolExpresion=ArbolBinario('')
    pilaPadres.incluir(arbolExpresion)
    arbolActual = arbolExpresion
    for i in listaSimbolos: 
        if i == '(':
            arbolActual.insertarIzquierdo('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoIzquierdo()
        elif i not in ['+', '-', '*', '/', ')']:
            arbolActual.asignarValorRaiz(int(i))
            padre = pilaPadres.extraer()
            arbolActual = padre
        elif i in ['+', '-', '*', '/']:
            arbolActual.asignarValorRaiz(i)
            arbolActual.insertarDerecho('')
            pilaPadres.incluir(arbolActual)
            arbolActual = arbolActual.obtenerHijoDerecho()
        elif i == ')':
            arbolActual = pilaPadres.extraer()
        else: 
            raise ValueError
    return arbolExpresion