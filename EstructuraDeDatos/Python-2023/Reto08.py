"""RETO EN CLASE N°8
Realizar un algoritmo que permita insertar elementos en un diccionario (Información de 3
estudiantes). El docente debe ser capaz de ingresar la siguiente información por teclado:
● Nombres de los estudiantes
● Nombre de la asignatura
● Nota del Laboratorio N°1
● Nota del Laboratorio N°2
La ponderación del Laboratorio N°1 es de un 30% del promedio final y el Laboratorio N°2
pondera 70% de la nota final.
El algoritmo debe arrojar toda la información ingresada más el promedio final ponderado.
Este promedio debe estar en un formato de punto flotante de máximo 1 decimal. """

indice = 0
Alumnos = dict()
estudiante = dict()#Creacion diccionario

for j in range(3):
    estudiante["nEstudiante"] = input("Ingrese nombre del estudiante: ")
    estudiante["nAsignatura"] = input("\nIngrese nombre de la asignatura: ")
    estudiante["lab1"] = float(input("\nIngrese nota del laboratorio 1: "))
    estudiante["lab2"]  = float(input("\nIngrese nota del laboratorio 2: "))
    i = False


    # Bucle para obligar que las notas esten entre 1 y 7
    for i in range(1):
        if 1.0 <= estudiante["lab1"] <= 7.0 and 1.0 <= estudiante["lab2"] <= 7.0:
            i = True
        else:
            print("Ingrese notas entre 1.0 y 7.0 ")
            i = False
            estudiante["lab1"] = float(input("\nIngrese nota del laboratorio 1: "))
            estudiante["lab2"]  = float(input("\nIngrese nota del laboratorio 2: "))



    notaPromedio= ((estudiante["lab1"] * 0.3) + (estudiante["lab2"] * 0.7))
    estudiante["nota"] = ("{:.1f}".format(notaPromedio))
    print("\nInformacion del estudiante: \n\nNombre del estudiante:", estudiante["nEstudiante"])
    print("Nombre Asignatura:", estudiante["nAsignatura"],"\nNota laboratorio Nª1:", estudiante["lab1"], "\nNota laboratorio Nª2:", estudiante["lab2"])



    informacion = list(estudiante.values())

    if indice == 0:
        Alumnos["primerEstudiante"] = informacion
        indice += 1
    elif indice == 1:
        Alumnos["segundoEstudiante"] = informacion
        indice += 1
    elif indice == 2:
        Alumnos["tercerEstudiante"] = informacion
        indice += 1
print("\n-----------------------------------------------------")
#Informacion primer estudiante
print("\nInformacion primer estudiante: ", "\nNombre: ",Alumnos["primerEstudiante"][0], "\nNombre Asignatura: ", Alumnos["primerEstudiante"][1])
print("Nota Lab. Nª1:", Alumnos["primerEstudiante"][2], "\nNota Lab. Nª2:", Alumnos["primerEstudiante"][3], "\nNota parcial:", Alumnos["primerEstudiante"][4])

#Informacion segundo estudiante
print("\nInformacion segundo estudiante: ", "\nNombre: ",Alumnos["segundoEstudiante"][0], "\nNombre Asignatura: ", Alumnos["segundoEstudiante"][1])
print("Nota Lab. Nª1:", Alumnos["segundoEstudiante"][2], "\nNota Lab. Nª2:", Alumnos["segundoEstudiante"][3], "\nNota parcial:", Alumnos["segundoEstudiante"][4])

#Informacion tercer estudiante
print("\nInformacion tercer estudiante: ", "\nNombre: ",Alumnos["tercerEstudiante"][0], "\nNombre Asignatura: ", Alumnos["tercerEstudiante"][1])
print("Nota Lab. Nª1:", Alumnos["tercerEstudiante"][2], "\nNota Lab. Nª2:", Alumnos["tercerEstudiante"][3], "\nNota parcial:", Alumnos["tercerEstudiante"][4])