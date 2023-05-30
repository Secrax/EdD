#Pedimos las filas y columnas de la primera matriz
import numpy
import random
#Datos de la matriz
f1 = int(input("\nIngrese filas de la primera matriz: "))#Filas primera matriz
c1 = int(input("Ingrese columnas de la primera matriz: "))#Columnas primera matriz
while f1 <= 0 and c1 <= 0:
    print("\nIngrese valores mayores a 0")
    f1 = int(input("\nIngrese filas de la primera matriz: "))#Filas primera matriz
    c1 = int(input("Ingrese columnas de la primera matriz: "))#Columnas primera matriz
    
f2 = 0
c2 = 0

print("\nDatos de la matriz 2, ingrese misma cantidad de filas y columnas que la anterior matriz")
while f1 != f2 and c1 != c2:

    f2 = int(input("Ingrese cantidad de filas: "))
    c2 = int(input("Ingrese cantidad de columnas: "))

m1 = numpy.zeros((f1,c1))#Matriz creada
m2 = numpy.zeros((f2,c2))#Matriz creada 
print("\nDatos de la matriz ")

#Llenado de la matriz
for i in range(f1):
    f1 = []
    for j in range(c1):
        m1[i][j] = random.randint(0,5)#Toma valores entre 0 y 5 incluyendolos
#Matriz 2
for i in range(f2):
    f2 = []
    for j in range(c2):
        m2[i][j] = random.randint(0,5)# toma valores entre 0 y 5 incluyendolos

#Suma de las matrizes con numeros randoms
print(" \nSuma de ambas matrizes")

m_suma = numpy.add(m1,m2)
    
print(m_suma)

print(" \nTercera matriz: ")
print("Ingrese misma cantidad de filas y columnas que la anterior matriz")

f3 = 0
c3 = 0
while f1 != f3 and c1 != c3:
    f3 = int(input("\nIngrese misma cantidad de filas: "))
    c3 = int(input("\nIngrese misma cantidad de columnas: "))

m3 = numpy.zeros((f3,c3))
#Creacion tercera matriz

for i in range(f3):
    f3 = []
    for j in range(c3):
        m3[i][j] = random.randint(0,5)
        

#Resta de la matriz m_suma y la tercera matriz creada
m_resultante = numpy.subtract(m3,m_suma)

print(m_resultante)