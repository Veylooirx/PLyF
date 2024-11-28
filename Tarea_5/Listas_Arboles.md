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

% División en cabeza y cola
Head = 1, Tail = [2, 3, 4].
