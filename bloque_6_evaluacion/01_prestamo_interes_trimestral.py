# Diagnóstico 1 - Préstamo con interés compuesto trimestral

def main():
    P = 0.0
    T = 0.0
    B = 0.0
    M = 0.0
    A = 0.0
    F = 0.0
    N = 0

    # Ejercicio: Diagnóstico 1 - Préstamo con interés compuesto trimestral
    # Datos: prestamo, tasa trimestral decimal, periodos y porcentaje de abono
    print(str("Monto del prestamo:"), sep="")
    P = float(input())
    print(str("Tasa trimestral en decimal (ej. 0.03):"), sep="")
    T = float(input())
    print(str("Numero de trimestres:"), sep="")
    N = int(input())
    print(str("Porcentaje de abono extraordinario (0 a 100):"), sep="")
    B = float(input())
    if P <= 0  or  T < 0  or  N < 0  or  B < 0  or  B > 100:
        print(str("Datos invalidos"), sep="")
    else:
        # Interes compuesto: monto = prestamo * (1 + tasa) ^ trimestres
        M = P * (1 + T) ** N
        A = M * B / 100
        F = M - A
        print(str("Monto antes del abono: $"), str(M), sep="")
        print(str("Abono extraordinario: $"), str(A), sep="")
        print(str("Monto final a cancelar: $"), str(F), sep="")

if __name__ == "__main__":
    main()
