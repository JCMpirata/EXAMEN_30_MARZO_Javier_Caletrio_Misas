from Pila_Nodos import Pila
from Pila_Nodos import SNode

def ordenar_lista(numeros):
    pila = []
    for i in numeros:
        nodo = SNode(i)
        pila.append(nodo)

    lista_corta = []

    while pila:
        nodo = pila.pop()
        lista_corta.append(nodo.elem)

    lista_corta.sort()
    return lista_corta


if __name__ == "__main__":
    numeros = [5, 2, 8, 1, 3, 9]
    print(ordenar_lista(numeros))





