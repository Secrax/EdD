import numpy as np
import random

filas = 3
columnas = 3
filas2 = 3
columnas2 = 3
matrix = np.zeros((filas,columnas))
matrix2 = np.zeros((filas,columnas))
for i in range(filas):
    for j in range(columnas):
        matrix[i][j] = random.randint(5,10) * -1
print(f"Primera matriz:\n{matrix}")


for i in range(filas):
    for j in range(columnas):
        matrix2[i][j] = random.randint(5,10) * -1
print(f"\nSegunda matriz:\n{matrix2}")


if columnas == filas2:
    matrix_resultante = np.dot(matrix,matrix2)
    print(f"\nMatriz resultante de la multiplicacion:\n{matrix_resultante}")

matrix_identidad = np.zeros((filas,columnas))

for i in range(filas):
    for j in range(columnas):
        if i == j:
            matrix_identidad[i][j] = 1
        elif i != j:
            matrix_identidad[i][j] = 0

        
print(f"\nMatriz identidad: \n{matrix_identidad}")

M = np.dot(matrix_resultante,matrix_identidad)
print(f"\nLa matriz resultante es:\n{M}")