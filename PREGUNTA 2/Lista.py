from Pila_Nodos import Pila
from Pila_Nodos import SNode


# Imprimir numeros en caso de que sea multiplo de 10 y menor que 200
def imprimir_multiplos(numeros):
    pila = Pila()
    for i in numeros:
        nodo = SNode(i)
        pila.push(nodo)

    while not pila.isEmpty():
        nodo = pila.pop()
        if nodo.elem % 10 == 0 and nodo.elem < 200:
            print(nodo.elem)

# Ordenar una lista de numeros
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
    numeros = [18, 50, 210, 80, 145, 333, 70, 30]
    print(imprimir_multiplos(numeros))
    print(ordenar_lista(numeros))





