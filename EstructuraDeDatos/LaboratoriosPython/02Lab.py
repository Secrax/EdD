#Pedimos las filas y columnas de la primera matriz
import numpy
import random
#Datos de la matriz
f = int(input("\nIngrese filas de la primera matriz: "))#Filas primera matriz
c = int(input("Ingrese columnas de la primera matriz: "))#Columnas primera matriz
while f <= 0 and c <= 0:
    print("\nIngrese valores mayores a 0")
    f = int(input("\nIngrese filas de la  matriz: "))#Filas primera matriz
    c = int(input("Ingrese columnas de la matriz: "))#Columnas primera matriz

m = numpy.zeros((f,c))#Matriz creada
#Matriz creada 
print(f"\nDatos de la matriz ")

#Llenado de la matriz
for i in range(f):
    f1 = []
    for j in range(c):
        m[i][j] = random.randint(0,10)#Toma valores entre 0 y 5 incluyendolos

print(m)
escalar = int(input("Ingrese entero que multiplicara a la matriz: "))


matriz = escalar * m

print(matriz)