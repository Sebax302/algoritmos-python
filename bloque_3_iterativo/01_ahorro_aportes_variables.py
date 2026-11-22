# Ahorro con aportes variables

def main():
    S = 0.0
    A = 0.0
    N = 0
    I = 0

    # Ejercicio: Ahorro con aportes variables
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese la cantidad de meses:"), sep="")
    N = int(input())
    # Proceso y cálculos
    if N <= 0:
        print(str("N debe ser mayor que cero"), sep="")
    else:
        S = 0
        for I in range(1, N + 1):
            print(str("Ingrese el aporte del mes "), str(I), str(":"), sep="")
            A = float(input())
            if A < 0:
                print(str("El aporte no puede ser negativo; se toma como 0"), sep="")
                A = 0
            S = (S + A) * 1.008
            print(str("Saldo del mes "), str(I), str(": $"), str(S), sep="")
        print(str("Saldo final: $"), str(S), sep="")

if __name__ == "__main__":
    main()
