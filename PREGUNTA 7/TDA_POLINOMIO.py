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
    
    def restar(self, polinomio):
        aux1 = self.cabeza
        aux2 = polinomio.cabeza
        polinomio_resultante = Polinomio()
        while aux1 is not None and aux2 is not None:
            if aux1.exponente == aux2.exponente:
                polinomio_resultante.agregar(aux1.coeficiente - aux2.coeficiente, aux1.exponente)
                aux1 = aux1.siguiente
                aux2 = aux2.siguiente
            elif aux1.exponente > aux2.exponente:
                polinomio_resultante.agregar(aux1.coeficiente, aux1.exponente)
                aux1 = aux1.siguiente
            else:
                polinomio_resultante.agregar(aux2.coeficiente, aux2.exponente)
                aux2 = aux2.siguiente
        while aux1 is not None:
            polinomio_resultante.agregar(aux1.coeficiente, aux1.exponente)
            aux1 = aux1.siguiente
        while aux2 is not None:
            polinomio_resultante.agregar(aux2.coeficiente, aux2.exponente)
            aux2 = aux2.siguiente
        return polinomio_resultante

