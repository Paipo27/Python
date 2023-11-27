# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 09:45:50 2023

@author: DAFEYEF
""" 

class Pila:
    def __init__(self):
        self.items=[]
        
    def estaVacia(self):
        return self.items==[]
    
    def incluir(self,item):
        self.items.append(item)
        
        
    def extraer(self): 
        return self.items.pop()
    
    def inspeccionar(self):
        return self.items[len(self.items)-1]
    
    def tamano(self):
        return len(self.items)
        
        