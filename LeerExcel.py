import pandas as pd

# Leer el archivo
df = pd.read_excel('Algoritmos.xlsx')

# Función para procesar el nombre de una columna
def process_column_name(column_name):
    if '.' in str(column_name):
        parts = str(column_name).split('.')
        return parts[0]
    return column_name

# Procesar los nombres de las columnas
df.columns = [process_column_name(col) for col in df.columns]

# Convertir el DataFrame a una lista de listas (matriz)
matrix_representation = df.values.tolist()

# Mostrar la matriz
print('Los canales ingresados son:')
for row in matrix_representation:
    print(row)