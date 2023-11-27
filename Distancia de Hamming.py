def distanciaHA(str1, str2):
      #Se verifica que las cadenas tengan la misma longitud
      if len(str1) != len(str2):
            print("Las cadenas deben tener la misma longitud")
            return None
      #se mira las cadenas y se busca la diferencia entre ellas para retornar el valor de la distancia de hamming
      return sum(c1 != c2 for c1, c2 in zip(str1, str2))

 


#Ejemplo de la distancia de Hamming
cadena1 = "perrito"
cadena2 = "calle"
Distancia = distanciaHA(cadena1, cadena2)
if Distancia != None:  
      print(f"La distancia de Hamming entre '{cadena1}' y '{cadena2}' es: {Distancia}")