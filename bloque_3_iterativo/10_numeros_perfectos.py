# Números perfectos
import math

def main():
    N = 0
    DIV = 0
    SUMA = 0

    # Ejercicio: Números perfectos
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese un numero entero positivo:"), sep="")
    N = int(input())
    # Proceso y cálculos
    while N <= 0:
        print(str("El numero debe ser mayor que 0"), sep="")
        print(str("Ingrese un numero entero positivo:"), sep="")
        N = int(input())
    SUMA = 0
    DIV = 1
    while DIV <= math.trunc(N / 2):
        if N % DIV == 0:
            SUMA = SUMA + DIV
        DIV = DIV + 1
    if SUMA == N  and  N > 1:
        print(str(N), str(" es un numero perfecto"), sep="")
    else:
        print(str(N), str(" no es un numero perfecto"), sep="")

if __name__ == "__main__":
    main()
