# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:22:59 2023

@author: DAFEYEF
"""

class Pila:
    def __init__(self):
        self.items=[]
        
    def estaVacia(self):
        return self.items==[]
    
    def incluir(self,item):
        self.items.insert(0,item)
    
    def extraer(self):
        return self.items.pop(0)
            
    def inspeccionar(self):
        return self.items[0]
    
    def tamano(self):
        return len(self.items)
        
    
    
    