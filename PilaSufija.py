from ProgaramaPila import Pila
def evaluacionNotacionSufija(expresionSufija):
    pilaOperandos= Pila()
    ListaSimbolos=expresionSufija.split()
    for simbolo in ListaSimbolos:
        if simbolo in "0123456789":
            pilaOperandos.incluir(int(simbolo))
        else:
            operando2=pilaOperandos.extraer()
            operando1=pilaOperandos.extraer()
            resultado=hacerAritmetica(simbolo,operando1,operando2)
            pilaOperandos.incluir(resultado)
    return pilaOperandos.extraer()

def hacerAritmetica(operador,operadorIzquierda,operadorDerecha):
    if operador=="*":
        return operadorIzquierda*operadorDerecha
    elif operador=="/":
        return operadorIzquierda/operadorDerecha
    elif operador=="+":
        return operadorIzquierda+operadorDerecha
    elif operador=="-":
        return operadorIzquierda-operadorDerecha