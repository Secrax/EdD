#Creacion de  matriz
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

print(f"El determinante de la matriz es: {determinante}\n")


print(f"Matriz que ocuparemos:\n{matrix}")
#f1 = int(input("Ingrese numero de filas: "))
#Matriz transpuesta
f1 = 3
c1 = 3#Lo mismo se puede poner a conveniencia el tamaño de la matriz 
matrixT = numpy.zeros((f1,c1))
for i in range(f1):
    for j in range(c1):
        matrixT[i][j] = matrix[j][i]

print(f"\nMatriz transpuesta:\n{matrixT}\n")

for i in range(f1):
    for j in range(c1):
        #nose como sacar la matriz adjunta
        matrizAD = None

#matrizI = matrizAD/determinante
matrizI =numpy.linalg.inv(matrix)
#print(f"\nMatriz adjunta:\n{matrizAD}\n")
I = numpy.round(numpy.dot(matrix,matrizI))

print(f"Comprobamos la formula: \n{I}")
