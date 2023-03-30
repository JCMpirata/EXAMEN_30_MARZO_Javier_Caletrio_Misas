
from Cola_Nodos import Cola
# DETERMINANTE 5X5 CON LA REGLA DE SARRUS EN UNA COLA DE NODOS EN FORMA RECURSIVA E ITERATIVA
    
def determinante(matriz):
    n = len(matriz)
    cola = Cola()
    for i in range(n):
        cola.encolar(matriz[0][i], 0, i)
    pila = [cola] + [Cola() for _ in range(1, n)]
    for i in range(1, n):
        for j in range(n):
            pila[i].encolar(matriz[i][j], i, j)
    return determinante_recursivo(pila, 1)

def determinante_recursivo(pila, det):
    if len(pila) == 0:
        return det
    cola = pila.pop(0)
    temp = 0
    while not cola.esta_vacia():
        valor, fila, columna = cola.desencolar()
        if fila == columna:
            temp += valor * det
        else:
            new_det = det * (-1 if fila < columna else 1)
            new_cola = Cola()
            while not cola.esta_vacia():
                v, f, c = cola.desencolar()
                if c != columna:
                    new_cola.encolar(v, f, c)
            new_pila = [new_cola for _ in range(len(pila))]
            temp += determinante_recursivo(new_pila, new_det * valor)
    return temp

def determinante_iterativo(matriz):
    n = len(matriz)
    cola = Cola()
    for i in range(n):
        cola.encolar(matriz[0][i], 0, i)
    pila = [cola] + [Cola() for _ in range(1, n)]
    for i in range(1, n):
        for j in range(n):
            pila[i].encolar(matriz[i][j], i, j)
    det = 0
    while not pila[0].esta_vacia():
        valor, fila, columna = pila[0].desencolar()
        if fila == columna:
            det += valor
        else:
            new_cola = Cola()
            while not pila[0].esta_vacia():
                v, f, c = pila[0].desencolar()
                if c != columna:
                    new_cola.encolar(v, f, c)
            pila[0] = new_cola
            det += (-1 if fila < columna else 1) * valor * determinante_recursivo(pila[1:], 1)
    return det
    

if __name__ == '__main__':
    matriz = [[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    print(determinante(matriz))
    print(determinante_iterativo(matriz))

