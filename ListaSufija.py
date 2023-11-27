from ProgaramaPila import Pila

import string

def infija_a_sufija(expresionInfija):
    Precedencia={}
    Precedencia["*"]=3
    Precedencia["/"]=3
    Precedencia["+"]=2
    Precedencia["-"]=2
    Precedencia["()"]=1
    PilaOperadores=Pila()
    listaSufija=[]
    ListaSimbolos=expresionInfija.split()
    for simbolo in ListaSimbolos:
        if simbolo in string.ascii_uppercase:
            listaSufija.append(simbolo)
        elif simbolo=='()':
            PilaOperadores.incluir(simbolo)
        elif simbolo==')':
            simboloTope =PilaOperadores.extraer()
            while simboloTope !='()':
                listaSufija.append(simboloTope)
                simboloTope=PilaOperadores.extraer()
        else:
            while(not PilaOperadores.estaVacia())and \
            (Precedencia[PilaOperadores.inspeccionar()]>=\
             Precedencia[simbolo]):
                listaSufija.append(PilaOperadores.extraer()) 
            PilaOperadores.incluir(simbolo)  
        while not PilaOperadores.estaVacia():
            listaSufija.append(PilaOperadores.extraer())
        return"u".join(listaSufija) 