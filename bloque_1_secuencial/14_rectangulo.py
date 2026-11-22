# Área y perímetro de un rectángulo

def main():
    L = 0.0
    A = 0.0
    AREA = 0.0
    P = 0.0

    # Ejercicio: Área y perímetro de un rectángulo
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el largo del rectangulo en metros:"), sep="")
    L = float(input())
    # Proceso y cálculos
    while L <= 0:
        print(str("El largo debe ser mayor que 0"), sep="")
        print(str("Ingrese el largo del rectangulo en metros:"), sep="")
        L = float(input())
    print(str("Ingrese el ancho del rectangulo en metros:"), sep="")
    A = float(input())
    while A <= 0:
        print(str("El ancho debe ser mayor que 0"), sep="")
        print(str("Ingrese el ancho del rectangulo en metros:"), sep="")
        A = float(input())
    AREA = L * A
    P = 2 * (L + A)
    print(str("El area del rectangulo es: "), str(AREA), str(" metros cuadrados"), sep="")
    print(str("El perimetro del rectangulo es: "), str(P), str(" metros"), sep="")

if __name__ == "__main__":
    main()
