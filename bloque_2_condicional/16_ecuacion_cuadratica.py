# Tipo de ecuación cuadrática

def main():
    A = 0.0
    B = 0.0
    C = 0.0
    D = 0.0

    # Ejercicio: Tipo de ecuación cuadrática
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el coeficiente A:"), sep="")
    A = float(input())
    print(str("Ingrese el coeficiente B:"), sep="")
    B = float(input())
    print(str("Ingrese el coeficiente C:"), sep="")
    C = float(input())
    # Proceso y cálculos
    if A == 0:
        print(str("No es una ecuacion cuadratica"), sep="")
    else:
        D = B ** 2 - 4 * A * C
        if D > 0:
            print(str("Tiene dos soluciones reales"), sep="")
        else:
            if D == 0:
                print(str("Tiene una solucion real"), sep="")
            else:
                print(str("No tiene soluciones reales"), sep="")

if __name__ == "__main__":
    main()
