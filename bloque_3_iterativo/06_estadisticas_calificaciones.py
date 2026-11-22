# Estadísticas de N calificaciones

def main():
    N = 0
    I = 0
    APR = 0
    REP = 0
    NOTA = 0.0
    SUMA = 0.0
    P = 0.0
    MAY = 0.0
    MEN = 0.0

    # Ejercicio: Estadísticas de N calificaciones
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese la cantidad de calificaciones:"), sep="")
    N = int(input())
    # Proceso y cálculos
    while N <= 0:
        print(str("La cantidad debe ser mayor que 0"), sep="")
        print(str("Ingrese la cantidad de calificaciones:"), sep="")
        N = int(input())
    SUMA = 0
    APR = 0
    REP = 0
    for I in range(1, N + 1):
        print(str("Ingrese la calificacion "), str(I), str(" (0 a 10):"), sep="")
        NOTA = float(input())
        while NOTA < 0  or  NOTA > 10:
            print(str("La nota debe estar entre 0 y 10"), sep="")
            print(str("Ingrese la calificacion "), str(I), str(" (0 a 10):"), sep="")
            NOTA = float(input())
        SUMA = SUMA + NOTA
        if I == 1:
            MAY = NOTA
            MEN = NOTA
        else:
            if NOTA > MAY:
                MAY = NOTA
            if NOTA < MEN:
                MEN = NOTA
        if NOTA >= 7:
            APR = APR + 1
        else:
            REP = REP + 1
    P = SUMA / N
    print(str("Promedio: "), str(P), sep="")
    print(str("Calificacion mayor: "), str(MAY), sep="")
    print(str("Calificacion menor: "), str(MEN), sep="")
    print(str("Cantidad de aprobados: "), str(APR), sep="")
    print(str("Cantidad de reprobados: "), str(REP), sep="")

if __name__ == "__main__":
    main()
