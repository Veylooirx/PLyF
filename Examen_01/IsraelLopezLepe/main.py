def f(x):
    return (x - 5) ** 2

def biseccion(a, b, tol, iteraciones=0, historial=[]):
    xm = (a + b) / 2.0
    fxm = f(xm)
    L = b - a
    x1 = a + L / 4
    x2 = b - L / 4
    fx1 = f(x1)
    fx2 = f(x2)

    historial.append((xm, fxm))
    print(f"Iteración {iteraciones}: xm = {xm:.6f}, Intervalo = [{a:.6f}, {b:.6f}]")

    if abs(b - a) < tol:  
        print(f"El mínimo aproximado se encuentra en: {xm:.6f}, después de {iteraciones} iteraciones.")
        return xm, iteraciones, historial

    if fx1 < fxm and fx1 < fx2:
        return biseccion(a, xm, tol, iteraciones + 1, historial)
    elif fx2 < fxm:
        return biseccion(xm, b, tol, iteraciones + 1, historial)
    else:
        return biseccion(x1, x2, tol, iteraciones + 1, historial)

A = 1
B = 10
E = 0.01  

raiz, iteraciones, historial = biseccion(A, B, E)
