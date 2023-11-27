def distanciaHA(str1, str2):
      #se mira las cadenas y se busca la diferencia entre ellas para retornar el valor de la distancia de hamming
      return sum(c1 != c2 for c1, c2 in zip(str1, str2))

 


#Ejemplo de la distancia de Hamming
cadena1 = "perrito"
cadena2 = "calle"
Distancia = distanciaHA(cadena1, cadena2)
print(f"La distancia de Hamming entre '{cadena1}' y '{cadena2}' es: {Distancia}")