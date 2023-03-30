# TDA  POLINOMIO DE MANERA RECURSIVA

class Nodo:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None

    def agregar(self, coeficiente, exponente):
        nuevo_nodo = Nodo(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            aux = self.cabeza
            while aux.siguiente is not None:
                aux = aux.siguiente
            aux.siguiente = nuevo_nodo

    def mostrar(self):
        aux = self.cabeza
        while aux is not None:
            print(aux.coeficiente, "x^", aux.exponente, end=" ")
            aux = aux.siguiente
        print()

    def evaluar(self, x):
        aux = self.cabeza
        resultado = 0
        while aux is not None:
            resultado += aux.coeficiente * x ** aux.exponente
            aux = aux.siguiente
        return resultado

