def encontrar(lista, elementoBuscado):
    for posicion, elemento in enumerate(lista):
        if elemento == elementoBuscado:
            return posicion
    return None  # Si no se encuentra el elemento, se devuelve None

# Ejemplo de uso
lista = [ [1, 2, 3], [4, 5, 6],12, [7, 8, 9]]
elementoBuscado = 12
posicion = encontrar(lista, elementoBuscado)

if posicion is not None:
    print(f"El elemento {elementoBuscado} se encuentra en la posición {posicion} de la lista principal.")
else:
    print(f"El elemento {elementoBuscado} no se encuentra en la lista principal.")
