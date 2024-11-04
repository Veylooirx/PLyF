def f(x):
    return (x - 5) ** 2

def biseccion(a, b, tol):
    iteraciones = 0
    historial = []

    while True:
        L = b - a
        xm = (a + b) / 2.0
        x1 = a + L / 4
        x2 = b - L / 4

        fxm = f(xm)
        fx1 = f(x1)
        fx2 = f(x2)

        historial.append((xm, fxm))
        print(f"Iteración {iteraciones}: xm = {xm:.6f}, Intervalo = [{a:.6f}, {b:.6f}]")

        if abs(b - a) < tol:
            print(f"El mínimo aproximado se encuentra en: {xm:.6f}, después de {iteraciones} iteraciones.")
            break
        if fx1 < fxm and fx1 < fx2:
            b = xm
        elif fx2 < fxm:
            a = xm
        else:
            a = x1
            b = x2

        iteraciones += 1

    return xm, iteraciones, historial

A = 1
B = 10
E = 0.01
raiz, iteraciones, historial = biseccion(A, B, E)
