import numpy
import random

filas = random.randint(3,5)#Es a eleccion puede variar el numero pero debe ser iguales
columnas = filas#Las filas con las columnas, osea filas = columnas
#matrix = numpy.zeros((filas,columnas))
matrix = []

#creamos la matriz

for i in range(filas):
    matrix.append([])
    for j in range(columnas):
        matrix[i].append(None)

#rellenamos la matriz

for i in range(filas):
    for j in range(columnas):
        matrix[i][j] = random.randint(0,5)

#Imprimir matriz original

"""if filas == 3:
    print(f"Matriz original:\n{matrix[0]} \n{matrix[1]} \n{matrix[2]}")
elif filas == 4:
    print(f"Matriz original:\n{matrix[0]} \n{matrix[1]} \n{matrix[2]} \n{matrix[3]}")
elif filas == 5:
    print(f"Matriz original:\n{matrix[0]} \n{matrix[1]} \n{matrix[2]} \n{matrix[3]} \n{matrix[4]}")"""
for i in range(filas):
    for j in range(filas):
        if j == len(matrix):
            print("|", end=" ")
        print("{0.8.2f".format(filas[j]),end = " ")
    print()
f1 = columnas
c1 = f1
#matrizT = numpy.zeros((f1,c1))
matrizT = []
for i in range(filas):
    matrizT.append([])
    for j in range(columnas):
        matrizT[i].append(None)
for i in range(f1):
    for j in range(c1):
        matrizT[i][j] = matrix[j][i] 

if filas == 3:
    print(f"Matriz Transpuesta:\n{matrizT[0]} \n{matrizT[1]} \n{matrizT[2]}")
elif filas == 4:
    print(f"Matriz Transpuesta:\n{matrizT[0]} \n{matrizT[1]} \n{matrizT[2]} \n{matrizT[3]}")
elif filas == 5:
    print(f"Matriz Transpuesta:\n{matrizT[0]} \n{matrizT[1]} \n{matrizT[2]} \n{matrizT[3]} \n{matrizT[4]}\n")

print("\nMatriz completa")
M = []
for elem in matrix: M.append(elem.copy())
for i in range(len(M)):
    for j in range(len(M)):
        M[i].append(1 if i == j else 0)

print("Matriz original - Matriz identidad")
print(f"\n{M}")