# Hipotenusa y área de un triángulo rectángulo
import math

def main():
    A = 0.0
    B = 0.0
    H = 0.0
    AR = 0.0

    # Ejercicio: Hipotenusa y área de un triángulo rectángulo
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el primer cateto:"), sep="")
    A = float(input())
    print(str("Ingrese el segundo cateto:"), sep="")
    B = float(input())
    # Proceso y cálculos
    if A <= 0  or  B <= 0:
        print(str("Los catetos deben ser mayores que cero"), sep="")
    else:
        H = math.sqrt(A ** 2 + B ** 2)
        AR = A * B / 2
        print(str("Hipotenusa: "), str(H), sep="")
        print(str("Area: "), str(AR), sep="")

if __name__ == "__main__":
    main()
