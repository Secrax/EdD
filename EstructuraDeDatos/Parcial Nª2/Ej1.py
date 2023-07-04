
#Lista Cicular doble Enlazada
class nodo:
    def __init__(self,nombre,numero,correo):
        self.nombre = nombre
        self.numero = numero
        self.correo = correo
        self.siguiente = None
        self.anterior = None
    
class CircularDobleEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def __unir_nodos(self):
        if self.primero !=None: #Si existe un dato para manipular
            self.primero.anterior = self.ultimo #con esto unimos el ultimo y primer nodo para hacer la lista circular
            self.ultimo.siguiente = self.primero #con esto decimos que el siguiente nodo del ultimo sera el primero

    #Si el primero es igual a None es que no tenemos nada
    def vacia (self):
        return self.primero == None
    
    def agregar_contacto(self,nombre,numero,correo):
        if self.vacia():
            self.primero = self.ultimo = nodo(nombre,numero,correo)
            #si esta vacia se agrega el dato al inicio


        else:
            #En caso de no estar vacia se crea un nodo y ese nodo apunta al siguiente
            auxiliar = nodo(nombre,numero,correo)
            auxiliar.siguiente = self.primero#le decimos que la vamos a crear en la primera posicion
            self.primero.anterior = auxiliar
            self.primero = auxiliar#luego el primero lo vamos a correr un nodo osea al siguiente

        self.__unir_nodos()#Con esto llamamos a la funcion y hacemos que el anterior al primero sera el ultimo
        #y el ultimo nodo el siguiente sera el primero

    def datos_lista_iniciofin(self):
        auxiliar = self.primero
        indice = 0
        while auxiliar:
            indice += indice
            print("[",auxiliar.nombre,",",auxiliar.numero, ",", auxiliar.correo, "]")
            auxiliar = auxiliar.siguiente
            if auxiliar == self.primero:
                break
            #Hacemos que recorra todos los nodos y este imprimiendo cada nodo
            #al momento que el auxiliar sea igual nuevamente al primer nodo o dato del primer nodo este rompera el ciclo while
            #y evitaremos que imprima eternamente la lista

    def eliminar_datos_inicio(self):
        if self.vacia():
            print("Lista vacia")

        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
            #El primero apunte a nada y el ultimo apunte a nada asi lo eliminamos en caso de que el ultimo y el primero sean el mismo dato

        else:
            self.primero = self.primero.siguiente
            #Le decimos que tome el valor del siguiente nodo
        self.__unir_nodos()
        #Y unimos los nodos
    def eliminar(self,dato):
        if self.vacia():
            print("La lista esta vacia")

        else:
            auxiliar = self.primero
            while auxiliar:
                auxiliar = self.auxiliar.siguiente
                if auxiliar == dato:
                    break

        self.unir_nodos()
    def buscar(self,dato):
        if self.vacia():
            print("La lista esta vacia")

        else:
            auxiliar = self.primero

            while auxiliar:#Mientras exista un dato
                if auxiliar == dato:
                    return True
                
                    #Le decimos que obtenga el dato del siguiente nodo y si llega a ser igual al primer nodo que retorne False
                auxiliar = auxiliar.siguiente
                if auxiliar == self.primero:
                    return False
    
    #Con este metodo solo imprime al usuario si esta o no vacia la lista.
    #El otro metodo vacia se encarga de verificar si esta o no vacia.
    def esta_vacia(self):
        if self.vacia():
            print("La lista esta vacia")
        
        else:
            print("La lista no esta vacia")

    
                



#A. Clases respectivas del problema
#B. Método para agregar un contacto a la lista
#C. Método para mostrar la lista de contactos
#D. Método para buscar un contacto por su nombre
#E. Método eliminar un contacto de la lista
#F. Método para verificar si la lista de contacto está vacía
i = True
lista_contactos = CircularDobleEnlazada()
while i == True:
    decision = int(input("\nIngrese que desea hacer:"
                     + "\n1.-Agregar contacto"
                     + "\n2.-Mostrar Contactos"
                     + "\n3.-Buscar Contacto"
                     + "\n4.-Eliminar Contacto"
                     + "\n5.-Verificar si esta vacia la lista de contactos"
                     + "\n6.-Salir del programa"
                     + "\nOpcion: "))
    
    if 1 <= decision <= 6:
        if decision == 1:
            contacto = str(input("\nIngrese nombre del contacto que quiera agregar: "))
            numero = int(input("INgrese su numero telefonico: "))
            correo = str(input("Ingrese su correo electronico: "))
            lista_contactos.agregar_contacto(contacto,numero, correo)
        elif decision == 2:
            lista_contactos.datos_lista_iniciofin()

        elif decision == 3:
            contacto = str(input("\nIngrese contacto a buscar: "))
            resultado = lista_contactos.buscar(contacto)
            if resultado == True:
                print("El contacto existe")
            
            else:
                print("El contacto no existe o no fue encontrado")


        elif decision == 4:
            eliminar = str(input("\nIngrese contacto que quiere eliminar: "))

        elif decision == 5:
            lista_contactos.esta_vacia()

        elif decision == 6:
            i = False