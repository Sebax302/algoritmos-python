# Valor futuro de una anualidad

def main():
    D = 0.0
    I = 0.0
    VF = 0.0
    TT = 0.0
    N = 0

    # Ejercicio: Valor futuro de una anualidad
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el deposito mensual:"), sep="")
    D = float(input())
    print(str("Ingrese la tasa mensual en decimal:"), sep="")
    I = float(input())
    print(str("Ingrese el numero de meses:"), sep="")
    N = int(input())
    # Proceso y cálculos
    TT = D * N
    if N <= 0  or  D < 0  or  I < 0:
        print(str("Datos no validos"), sep="")
    else:
        if I == 0:
            VF = TT
        else:
            VF = D * (((1 + I) ** N - 1) / I)
        print(str("Total depositado: $"), str(TT), sep="")
        print(str("Valor futuro: $"), str(VF), sep="")

if __name__ == "__main__":
    main()
