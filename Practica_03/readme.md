# Explicación del Código

Este código incluye varias funciones y una clase diseñadas para manipular listas y árboles binarios en Python. A continuación, se describe cada componente del código:

## Funciones para Listas

### 1. `concatenar(lista1, lista2)`
Esta función concatena dos listas de manera recursiva.

**Cómo funciona:**
- Si `lista1` está vacía (`not lista1`), retorna `lista2`.
- Si no está vacía, toma el primer elemento de `lista1` (`lista1[0]`), lo agrega al resultado de concatenar el resto de `lista1` (`lista1[1:]`) con `lista2`.

**Ejemplo:**
```python
concatenar([1, 2, 3], [4, 5, 6])
 esultado: [1, 2, 3, 4, 5, 6]

### 2. `pertenece(elemento, lista)`
Verifica si un elemento pertenece a una lista de forma recursiva.

**Cómo funciona:**
- Si la lista está vacía, retorna `False`.
- Si el primer elemento de la lista es igual al `elemento`, retorna `True`.
- Si no, llama a `pertenece` con el resto de la lista (`lista[1:]`).

**Ejemplo:**
```python
pertenece(3, [1, 2, 3])
# Resultado: True
pertenece(4, [1, 2, 3])
# Resultado: False

### Clase para Árbol Binario

#### `Nodo`
Representa un nodo en un árbol binario.

**Atributos:**
- `valor`: Almacena el valor del nodo.
- `izquierdo`: Referencia al nodo hijo izquierdo (puede ser `None`).
- `derecho`: Referencia al nodo hijo derecho (puede ser `None`).

**Constructor:**
```python
class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
arbol = Nodo(1, Nodo(2), Nodo(3))

