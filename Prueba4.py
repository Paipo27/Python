# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:20:32 2023

@author: DAFEYEF
"""

from ProgaramaPila import Pila

def verificarSimbolos(cadenaSimbolos):
    p=Pila()
    balanceados=True
    indice=0
    while indice <len(cadenaSimbolos) and balanceados:
        simbolo =cadenaSimbolos[indice]
        if simbolo in "([{":
            p.incluir(simbolo)
        elif  simbolo==')]}':
            tope=p.extraer()
            if not parejas(tope,simbolo):
                    balanceados=False
        indice=indice+1
    if balanceados and p.estaVacia():
        return True
    else:
        return False
def parejas(simboloApertura,simboloCierre):
    apertura="([{"
    cieeres=")]}"
    return apertura.index(simboloApertura)==cieeres.index(simboloCierre)