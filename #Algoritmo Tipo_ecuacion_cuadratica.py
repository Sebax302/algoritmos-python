#Algoritmo Tipo_ecuacion_cuadratica
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a == 0:
    print("No es una ecuación cuadrática porque a debe ser distinto de cero.")
else:
    discriminante = b**2 - 4 * a * c

    if discriminante > 0:
        print("Tiene dos soluciones reales.")
    elif discriminante == 0:
        print("Tiene una solución real.")
    else:
        print("No tiene soluciones reales.")