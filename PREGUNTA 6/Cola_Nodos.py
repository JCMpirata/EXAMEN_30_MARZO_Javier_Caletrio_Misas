class Nodo:
    def __init__(self, valor, fila, columna, siguiente=None):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.siguiente = siguiente

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0
        
    def esta_vacia(self):
        return self.frente is None
        
    def encolar(self, valor, fila, columna):
        nodo = Nodo(valor, fila, columna)
        if self.esta_vacia():
            self.frente = nodo
        else:
            self.final.siguiente = nodo
        self.final = nodo
        self.tamaño += 1
        
    def desencolar(self):
        if self.esta_vacia():
            return None
        nodo = self.frente
        self.frente = nodo.siguiente
        self.tamaño -= 1
        if self.esta_vacia():
            self.final = None
        return nodo.valor, nodo.fila, nodo.columna