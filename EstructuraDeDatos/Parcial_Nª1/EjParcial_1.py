import numpy as np
import random

filas = 3
columnas = filas
matrix = np.zeros((filas,columnas))

for i in range(filas):
    for j in range(columnas):
        matrix[i][j] = random.randint(5,10)
print(f"La matriz que ocuparemos:\n{matrix}")
determinante = np.linalg.det(matrix)
print(f"El determinante es:\n{determinante}")