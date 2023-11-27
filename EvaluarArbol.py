from EvaluacionAritmeticaArbol import evaluar
from ArbolSintactico import construirArbolAnalisis

miArbol=construirArbolAnalisis("( 1 + ( 3 * ( 5 - 2 ) ) )")
print(evaluar(miArbol))