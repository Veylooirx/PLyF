def concatenar(lista1, lista2):
    if not lista1:  
        return lista2
    return [lista1[0]] + concatenar(lista1[1:], lista2)

def pertenece(elemento, lista):
    if not lista:  
        return False
    if lista[0] == elemento:  
        return True
    return pertenece(elemento, lista[1:])  

def longitud(lista):
    if not lista:  
        return 0
    return 1 + longitud(lista[1:])  

class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho

def in_orden(nodo):
    if nodo is None:  
        return []
    return in_orden(nodo.izquierdo) + [nodo.valor] + in_orden(nodo.derecho)

def altura(nodo):
    if nodo is None:  
        return 0
    return 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))

if __name__ == "__main__":
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    print("Concatenación de listas:", concatenar(lista1, lista2))
    print("Pertenencia de 3 en lista1:", pertenece(3, lista1))
    print("Longitud de lista1:", longitud(lista1))

    arbol = Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3))
    
    print("Recorrido in-orden del árbol:", in_orden(arbol))
    print("Altura del árbol:", altura(arbol))
