import numpy
import random

print("Creación de matriz 1")
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m = numpy.zeros((filas, columnas))
for i in range(filas):
    for j in range(columnas):
        m[i][j] = random.randrange(1,6)


m2 = numpy.zeros(filas,columnas)
for i in range(filas):
    for j in range(columnas):
        m[i][j] = random.randrange(1,6)

m3  = numpy.zeros(filas, columnas)
for i in range (filas):
    for j in range(columnas):
        m3[i][j] = m[i][j] + m2[i][j]
    print(m3)


for escalar in range(1,10):
    escalar = float(input("Ingrese numero: "))

matriz_resultante = escalar * m3

m4 = numpy.zeros(filas,columnas)
h = 0
for h in range(1):
    filas2 = int(input("Ingrese numero de filas: "))
    columnas2 = int(input("Ingrese numero de columnas: "))
    if filas2 == columnas:
        h = h + 1
    print("Ingrese de nuevo los datos deben ser compatibles lo datos para la multiplicacion\n")



for i in range(filas2):
    for j in range(columnas2):
        m4[i][j] = float(input(f"Ingrese numero en la posicion{i},{j}"))
    print(m4)
matriz_multiplicativa = numpy.dot(matriz_resultante,m4)
print(f"Matriz resultante final:\n{matriz_multiplicativa}")