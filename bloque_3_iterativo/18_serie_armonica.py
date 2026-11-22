# Suma de la serie armónica

def main():
    S = 0.0
    N = 0
    I = 0

    # Ejercicio: Suma de la serie armónica
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese N:"), sep="")
    N = int(input())
    # Proceso y cálculos
    if N <= 0:
        print(str("N debe ser mayor que cero"), sep="")
    else:
        S = 0
        for I in range(1, N + 1):
            S = S + 1 / I
        print(str("Suma de la serie: "), str(S), sep="")

if __name__ == "__main__":
    main()
