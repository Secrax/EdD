#Lista Enlazada
import math

class nodo():
    def __init__(self, codigo,nombre,descripcion,cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.siguiente = None
        self.anterior = None


class ListaEnlazada():
    def __init__(self):
        self.primero = None

    def agregar_nodo(self,codigo,nombre,descripcion,cantidad):
        if self.vacia():
            self.primero = self.ultimo = nodo(codigo,nombre,descripcion,cantidad)

        else:
            auxiliar = nodo(codigo,nombre,descripcion,cantidad)
            auxiliar.siguiente = self.primero
            self.primero.anterior = auxiliar
            self.primero = auxiliar

    def __str__(self):
        String = "["
        auxiliar = self.primero
        for i in range(len(self)):
            String += str(auxiliar.dato)
            if i != len(self) - 1:
                String += str(", ")
            auxiliar = auxiliar.siguiente
        String += "]"

        return String

    def vacia (self):
        return self.primero == None
    
    def esta_vacia(self):
        if self.vacia():
            print("La lista esta vacia")
        
        else:
            print("La lista no esta vacia")

    def buscar(self,codigo):
        if self.vacia():
            print("La lista esta vacia")

        else:
            auxiliar = self.primero

            while auxiliar:#Mientras exista un dato
                if auxiliar == codigo:
                    return print("[",auxiliar.codigo,",",auxiliar.nombre,",",auxiliar.descripcion,",",auxiliar.cantidad,"]")
                

                auxiliar = auxiliar.siguiente
                if auxiliar == self.primero:
                    return print("No se encontro un articulo con ese codigo")

