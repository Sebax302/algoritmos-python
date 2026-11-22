# Número de Armstrong de tres dígitos
import math

def main():
    N = 0
    T = 0
    D = 0
    S = 0

    # Ejercicio: Número de Armstrong de tres dígitos
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese un numero de tres digitos:"), sep="")
    N = int(input())
    # Proceso y cálculos
    if N < 100  or  N > 999:
        print(str("Debe ingresar un numero de tres digitos"), sep="")
    else:
        T = N
        S = 0
        while T > 0:
            D = T % 10
            S = S + D ** 3
            T = math.trunc(T / 10)
        if S == N:
            print(str(N), str(" es un numero de Armstrong"), sep="")
        else:
            print(str(N), str(" no es un numero de Armstrong"), sep="")

if __name__ == "__main__":
    main()
