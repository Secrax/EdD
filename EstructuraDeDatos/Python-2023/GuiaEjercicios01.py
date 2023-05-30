#Creacion matriz de 5x5
import random
import numpy as np

columnas = int(5)
filas = int(5)
matrix = np.zeros((filas,columnas))
for i in range(filas):
    filas = []
    for j in range(columnas):
        matrix[i][j] = random.randint(0,5)
print(f"Matriz resultante:\n {matrix}")

#suma de columnas
lista = []
filas2 = int(5)
suma = -1
for j in range (columnas):
    columnas = []
    for i in range(filas2):
        lista.append(matrix[i][j])#
        if i == 4:
            if suma == -1:#Esto es para el primer caso para que al final alla una comparacion con la segunda suma
                primeraSuma = sum(lista)#y se quede con la mayor de las sumas
                suma = 0
                lista = []
            else:
                suma = sum(lista)
                lista = []
                if suma > primeraSuma:
                    primeraSuma = suma
            

"""suma1 = int(sum(lista[0]))
suma2 = int(sum(lista[1]))
suma3 = int(sum(lista[2]))
suma4 = int(sum(lista[3]))
suma5 = int(sum(lista[4]))
listaSumas = [suma1,suma2,suma3,suma4,suma5]"""

"""mayor = listaSumas[0]
for n in listaSumas:
    if n > mayor:
        mayor = n"""
  
print(f"\nLa suma mayor de las columnas es: {primeraSuma}")

#print(f"\nLas sumas que nos dio son: \n1.-{suma1}\n2.-{suma2}\n3.-{suma3}4.-{suma4}\n5.-{suma5}")


#Suma de todas las filas
print(f"\nMatriz a usar:\n\n{matrix}\n")
f1 = 5
c1 = 5
indice = -1
listaValores = []
listaMenor = []
for i in range(f1):
    f1 = []
    for j in range(c1):
        listaValores.append(matrix[i][j])
        listaMenor.append(matrix[i][j])
        if j == 4:
            if indice == -1:
                sumaMenor = sum(listaMenor)
                indice = 0
                listaMenor = []
            else:
                indice = sum(listaMenor)
                if indice < sumaMenor:
                    sumaMenor = indice
                    listaMenor = []
                    #esta incompleto al momento de sacar la suma de las filas no devuelve el valor correcto
                


        


sumaFilas = sum(listaValores)
print(f"La suma de las filas es: {sumaFilas}\n")

print(f"La suma mas baja entre todas las filas es: {sumaMenor}")