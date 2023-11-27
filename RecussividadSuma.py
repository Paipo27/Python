def sumaLista(numLista):
    if len(numLista)==1:
        return numLista[0]
    else:
        return numLista[0]+sumaLista(numLista[1:])
    
print(sumaLista([1,3,5,7,9]))