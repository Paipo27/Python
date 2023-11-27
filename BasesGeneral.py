# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:22:47 2023

@author: DAFEYEF
"""

from ProgaramaPila import Pila
 
 
def convertirBase(numeroDecimal,base):
     digitos="0123456789ABCDEF"
     
     pilaResiduo=Pila()
     
     while numeroDecimal>0:
         residuo=numeroDecimal%base
         pilaResiduo.incluir(residuo)
         numeroDecimal=numeroDecimal//base
         
         
     nuevaCdena=""
    
     while not pilaResiduo.estaVacia():
            nuevaCdena=nuevaCdena+digitos[pilaResiduo.extraer()]
            
     return nuevaCdena
     
 
 