# Inversión de un número
import math

def main():
    N = 0
    T = 0
    D = 0
    INV = 0

    # Ejercicio: Inversión de un número
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese un numero entero positivo:"), sep="")
    N = int(input())
    # Proceso y cálculos
    if N <= 0:
        print(str("El numero debe ser positivo"), sep="")
    else:
        T = N
        INV = 0
        while T > 0:
            D = T % 10
            INV = INV * 10 + D
            T = math.trunc(T / 10)
        print(str("Numero invertido: "), str(INV), sep="")

if __name__ == "__main__":
    main()
