import numpy
import random

filas = 3#Es a eleccion puede variar el numero pero debe ser iguales
columnas = 3#Las filas con las columnas, osea filas = columnas
matrix = numpy.zeros((filas,columnas))

for i in range(filas):
    filas = []
    for j in range(columnas):
        matrix[i][j] = random.randint(0,5)#Esto tambien es variable en el rango que uno quiera
        #pero por comodidad lo deje en un rango de 0 hasta 5
valor = numpy.linalg.det(matrix)
determinante = round(valor)
print(f"El determinante que nos da es: {determinante}")