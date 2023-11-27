"Funcion recursiva que ordena los datos de menor a mayor"
def insercionSort(A, n):
    "Caso base de la funcion recursiva"
    if n <= 1:
        return
    "Llamado recursivo a la funcion "
    insercionSort(A, n-1)
    "Se guarda el ultimo dato de la lista en una variable"
    mayor = A[n-1]
    j = n-2
    "Ciclo que ordena los datos de menor a mayor"
    while j >= 0 and mayor < A[j]:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = mayor

"Funcion que llama a la funcion recursiva y retorna los datos ordenados"
def insercionSort2(A):
 insercionSort(A, len(A))
 return A

"Datos y llamado a la funcion insercionSort2"
Datos =[8, 2, 5,3 ,6 ,4 ,7, 1]
print(insercionSort2(Datos))