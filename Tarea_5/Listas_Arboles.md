# Desarrollo de Listas y Árboles en Programación Lógica

## Introducción

La **programación lógica** es un paradigma de programación que se enfoca en **describir qué se debe lograr** en lugar de especificar los pasos exactos para lograrlo. Este enfoque declarativo utiliza lógica matemática para expresar hechos, reglas y consultas, permitiendo que un motor de inferencia derive soluciones. Aunque Python no es un lenguaje de programación lógica por diseño, sus características permiten emular conceptos clave de este paradigma.

En este documento, exploraremos:

1. **Listas**: cómo representarlas, trabajar con ellas y realizar operaciones comunes de manera recursiva.
2. **Árboles**: cómo modelarlos, construir operaciones sobre ellos y realizar recorridos.
3. Las diferencias fundamentales entre la programación lógica y la programación funcional.

---

## 1. Listas en Programación Lógica y Python

### 1.1. Representación de Listas

En programación lógica, una lista se define como una secuencia ordenada de elementos. A menudo, las listas se representan mediante dos partes principales:

- **Cabeza (Head)**: el primer elemento de la lista.
- **Cola (Tail)**: una sublista que contiene el resto de los elementos.

Esta estructura facilita un procesamiento recursivo, ya que muchas operaciones pueden reducirse a operaciones sobre la cabeza y recursiones sobre la cola.

#### Ejemplo en Prolog:
```prolog
% Lista completa
[1, 2, 3, 4].
```
% División en cabeza y cola
Head = 1, Tail = [2, 3, 4].

En Python, las listas se representan como arreglos dinámicos. La división en Head y Tail puede hacerse mediante desempaquetado:

```python
lista = [1, 2, 3, 4]
```

# División en Head y Tail
head, *tail = lista  # head = 1, tail = [2, 3, 4]

# Operaciones Comunes con Listas
La concatenación de listas en programación lógica se implementa de forma recursiva:
```python
def concatenar(lista1, lista2):
    if not lista1:  # Caso base: lista1 está vacía
        return lista2
    return [lista1[0]] + concatenar(lista1[1:], lista2)
# Ejemplo de uso
lista1 = [1, 2]
lista2 = [3, 4]
print(concatenar(lista1, lista2))  # Salida: [1, 2, 3, 4]
```

Pertenencia de un Elemento
Determinar si un elemento pertenece a una lista es una operación común:

```python
def pertenece(elemento, lista):
    if not lista:  # Caso base: lista vacía
        return False
    if lista[0] == elemento:  # El elemento coincide con la cabeza
        return True
    return pertenece(elemento, lista[1:])  # Busca en la cola

# Ejemplo de uso
print(pertenece(3, [1, 2, 3, 4]))  # Salida: True
print(pertenece(5, [1, 2, 3, 4]))  # Salida: False
```

Calcular la longitud de una lista también puede hacerse de manera recursiva:

```python
def longitud(lista):
    if not lista:  # Caso base: lista vacía
        return 0
    return 1 + longitud(lista[1:])  # Suma 1 y recursión sobre la cola
# Ejemplo de uso
print(longitud([1, 2, 3, 4]))  # Salida: 4
```

## 2. Árboles en Programación Lógica y Python

# Representación de Árboles
En programación lógica, los árboles suelen representarse como estructuras recursivas. Un árbol binario puede definirse como:

Árbol vacío: representado por None.
Árbol no vacío: un nodo raíz con subárboles izquierdo y derecho.
Podemos modelar un árbol binario con clases:

```python
class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
# Creación de un árbol binario
arbol = Nodo(1, Nodo(2), Nodo(3))
```

## Operaciones Comunes con Árboles
# Recorrido In-Orden
El recorrido in-orden visita el subárbol izquierdo, luego el nodo raíz, y finalmente el subárbol derecho.

```python
def in_orden(nodo):
    if nodo is None:
        return []
    return in_orden(nodo.izquierdo) + [nodo.valor] + in_orden(nodo.derecho)

# Ejemplo de uso
print(in_orden(arbol))  # Salida: [2, 1, 3]
```
# Altura del Árbol
La altura de un árbol se define como la longitud del camino más largo desde la raíz hasta una hoja.

```python
def altura(nodo):
    if nodo is None:
        return 0
    return 1 + max(altura(nodo.izquierdo), altura(nodo.derecho))

# Ejemplo de uso
print(altura(arbol))  # Salida: 2
```
## Diferencias entre Programación Lógica y Programación Funcional


### 1. **Definición**

#### **Programación Lógica**
- Paradigma basado en la lógica matemática.
- Consiste en declarar hechos y reglas, dejando que el motor de inferencia del lenguaje encuentre soluciones.
- Usado principalmente en la resolución de problemas, inteligencia artificial y bases de conocimiento.

## 2. Enfoque
**Programación Lógica**
Se basa en la declaración de qué se desea resolver.
La ejecución depende de un motor de inferencia que evalúa las reglas y los hechos.

**Programación Funcional**
Se enfoca en cómo transformar datos utilizando funciones.
La ejecución implica la evaluación de funciones en forma explícita.

## 3. Lenguajes Representativos
# Programación Lógica
Prolog.
Datalog.

# Programación Funcional
Haskell.
Lisp.
Scala.
Elixir.

Conclusión
Tanto las listas como los árboles son estructuras fundamentales en programación lógica, ya que facilitan la representación de relaciones jerárquicas y secuenciales. En Python, podemos replicar estos conceptos utilizando recursión, clases y desempaquetado. Aunque la programación lógica y la funcional comparten principios declarativos, se diferencian en cómo abordan la transformación de datos y la relación entre ellos.

Este enfoque muestra cómo conceptos abstractos de programación lógica pueden implementarse en Python, proporcionando un puente entre paradigmas.