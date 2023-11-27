def generar_matriz(*canales):
    estados = ["000", "100", "010", "110", "001", "101", "011", "111"]
    # Inicializamos la matriz con ceros
    matriz = [[0.0 for _ in range(8)] for _ in range(8)]

    for idx, estado in enumerate(estados):
        count = sum([1 for i in range(len(canales[0]) - 1) if 
                     all([canal[i] == int(bit) for canal, bit in zip(canales, estado)])])
        if count == 0:
            continue

        for j, next_estado in enumerate(estados):
            occurrences = sum([1 for i in range(len(canales[0]) - 1) if 
                               all([canal[i] == int(estado[k]) for k, canal in enumerate(canales)]) and 
                               all([canal[i+1] == int(next_estado[k]) for k, canal in enumerate(canales)])])
            matriz[idx][j] = round(float(occurrences) / count, 2)

    return matriz

def mostrar_matriz(matriz):
    estados = ["000", "100", "010", "110", "001", "101", "011", "111"]

    # Encabezado
    encabezado = "      "  # espacio inicial
    for estado in estados:
        encabezado += "{:^7}".format(estado)
    print(encabezado)
    
    for i, estado_row in enumerate(estados):
        fila = estado_row + " "
        for j, estado_col in enumerate(estados):
            valor = matriz[i][j]
            fila += "{:^7.2f}".format(valor)
        print(fila)

canal_A = [0,1,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,1]
canal_B = [0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,0,0,0]
canal_C = [0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0]

matriz_resultante = generar_matriz(canal_A, canal_B, canal_C)
mostrar_matriz(matriz_resultante)
