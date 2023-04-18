from Nodo import Nodo

class Lista_doble:
    def __init__(self) -> None:
        self.inicio = None
        self.final = None

    def Agregar(self,dato):
        
        if self.inicio is None:
            nuevo = Nodo(dato)
            self.inicio = nuevo
            return
        nodo = self.inicio
        while nodo.siguiente is not None:
            nodo = nodo.siguiente
        nuevo = Nodo(dato)
        nodo.siguiente = nuevo
        nuevo.anterior = nodo
        nuevo.siguiente = None

    def Ordenar_lista(self):
        nodo = self.inicio
        while nodo is not None:
            mayor = nodo.siguiente
            while mayor is not None:
                if mayor.dato < nodo.dato:
                    mayor.dato, nodo.dato = nodo.dato, mayor.dato
                mayor = mayor.siguiente
            nodo = nodo.siguiente

    def Eliminar_repetidos(self):      
        if self.inicio is None:
            print("no hay datos")
            return
        nodo = self.inicio
        while nodo is not None:
            nodo_next = nodo.siguiente
            i = 0
            while nodo_next is not None:
                if nodo_next.dato == nodo.dato:
                    i += 1
                    if i > 1:
                        nodo_next.anterior.siguiente = nodo_next.siguiente
                        nodo_next.siguiente.anterior = nodo_next.anterior
                nodo_next = nodo_next.siguiente
            nodo = nodo.siguiente