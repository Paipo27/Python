from ColaDoble import ColaDoble1
 

def verificarPalindromo(cadena):
    
    ColaDobleCaracteres=ColaDoble1()
    for caracter in cadena:
        ColaDobleCaracteres.agregarFinal(caracter)
    
    aunIguales= True

    while ColaDobleCaracteres.tamano() > 1 and aunIguales:
        primero=ColaDobleCaracteres.removerFrente()
        ultimo=ColaDobleCaracteres.removerfinal()
        if primero != ultimo:
            aunIguales=False

    return aunIguales
print(verificarPalindromo("lsdkjfskf"))
print(verificarPalindromo("radar"))
