def distanciaHA(str1, str2):
    # Aseguramos que las cadenas tengan la misma longitud
    if len(str1) != len(str2):
        raise ValueError("Las cadenas deben tener la misma longitud para la distancia de Hamming.")

    # Contamos la cantidad de caracteres diferentes en las mismas posiciones
    sum(c1 != c2 for c1, c2 in zip(str1, str2))
    return sum
# Ejemplo de uso
cadena1 = "casa"
cadena2 = "calle"
resultado_hamming = distanciaHA(cadena1, cadena2)
print(f"La distancia de Hamming entre '{cadena1}' y '{cadena2}' es: {resultado_hamming}")