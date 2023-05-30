import random
import numpy as np

def imprimirMatriz(M):
    for fila in M:
        for k in range (len(fila)):
            if k == len(M):
                print("|", end =" ")
            print("{0:8.2f}".format(fila[k]), end = " ")
        print()
    print()

def inversa(A):
    print("Matriz original")
    imprimirMatriz(A)
    M = []
    for elem in A:
        M.append(elem.copy())
    for fila in range(len(M)):
        for col in range(len(M)):
            M[fila].append (1 if fila == col else 0)
    
    print("Matriz original ampliada")
    imprimirMatriz(M)
    for indice in range(len(M)-1):
        if M[indice][indice] == 0:
            print("indice con valor 0",indice,"hay que buscar una fila para cambiarla")
            for fila in range(indice + 1, len(M)):
                if M[fila][indice] != 0:
                    print("Sumar la fila: indice:",indice,",fila",fila)
                    for columna in range(indice,len(M[fila])):
                        M[indice][columna] = M[fila][columna]
                    imprimirMatriz(M)
                    break
            if M[indice][indice] == 0:
                return None
        for fila in range(indice + 1 , len(M)):
            determinante = M[fila][indice] / M[indice][indice]
            print("Indice:",indice,",Fila:",filas,",Determinante:",M[fila][indice],"/",M[indice][indice], "=",determinante)
            if determinante != 0:
                for columna in range(indice,len(M[fila])):
                    M[fila][columna] = M[indice][columna] * determinante
                imprimirMatriz(M)
    print("Reducimos la matriz,poniendo 0 arriba\n")
    for fila in range(len(M)):
        print("Mirando fila:",fila)
        for columna in range(fila + 1 , len(M)):
            print("Mirando fila:",fila,"columna:",columna)
            if M[columna][columna] != 0:
                determinante = M[fila][columna] / M[columna][columna]
                print("Determinante:",M[fila][columna],"/",M[columna][columna],"=",determinante)
                for colAux in range(columna , len(M) * 2):
                    M [fila][colAux] -= M[columna][colAux] * determinante
                imprimirMatriz(M)
            else:
                print("No se puede realizar mas acciones")
        imprimirMatriz(M)
    
    print("Convirtiendo la diagonal principal en 1")
    for fila in range(len(M)):
        factor = M[fila][fila]
        for columna in range (len(M[fila])):
            M[fila][columna] /= determinante
    imprimirMatriz(M)

    print("Eliminando la matriz a la izquierda")
    for fila in range(len(M)):
        M[fila] = M[fila][len(M):]
    imprimirMatriz(M)

    return M
#*
filas = random.randint(3,5)#Es a eleccion puede variar el numero pero debe ser iguales
columnas = filas#Las filas con las columnas, osea filas = columnas
matrix = []

#Creacion matriz
for i in range(filas):
    matrix.append([])
    for j in range(columnas):
        matrix[i].append(None)

#rellenamos la matriz

for i in range(filas):
    for j in range(columnas):
        matrix[i][j] = random.randint(0,5)#Es un rango pero puede ser con numeros mucho mayores


I = inversa(matrix)
print("Matriz inversa:")
imprimirMatriz(I)

#Comprobacion si es la matriz inversa

IconNumpy = np.linalg.inv(matrix)
print("Matriz inversa con numpy")
print(IconNumpy)