import numpy
import random
print("Multiplicacion de matrizes")
f1 = int(input("\nIngrese numero de filas de la primera matriz: "))
c1 = int(input("Ingrese numero de columnas de la primera matriz: "))
m1 = numpy.zeros((f1,c1))
for i in range(f1):
    for j in range(c1):
        m1[i][j] = random.randint(-10,10)
m1_traspuesta = numpy.transpose(m1)
print(m1)

f2 = int(input("\nIngrese numero de filas de la segunda matriz: "))
c2 = int(input("Ingrese numero de columnas de la segunda matriz: "))
m2 = numpy.zeros((f2,c2))
for i in range(f2):
    for j in range(c2):
        m2[i][j] = random.randint(-10,10)
print(m2)
m2_traspuesta = numpy.transpose(m2)
if c1 == f2:
    m_resultante = numpy.dot(m1,m2)
    print("\nLa matriz resultante:\n", m_resultante)
else:
    print("\nNo se puede ejecutar la multiplicacion")
print("\nMultiplicacion de Transpuesta")
if c2 == f1:
    transpuesta_resultante = numpy.dot(m1_traspuesta,m2_traspuesta)
    print("\nLa matriz resultante:\n",transpuesta_resultante)
else:
    print("\nNo se puede ejecutar la multiplicacion")


print("\nComprobacion de la transpuesta de la transpuesta es la matriz original")
print("\nMatriz original\n",m1)
print("\nMatriz traspuesta\n",m1_traspuesta)
m1_dobleT = numpy.transpose(m1_traspuesta)
print("\nMatriz traspuesta de la transpuesta\n",m1_dobleT)