# Aprobados o reprobados

def main():
    N = 0
    X = 0
    A = 0
    R = 0
    NOTA = 0.0

    # Ejercicio: Aprobados o reprobados
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el numero de alumnos:"), sep="")
    N = int(input())
    # Proceso y cálculos
    A = 0
    R = 0
    while N <=0:
        print(str("La cantidad ingresada no puede ser menor ni igual a 0"), sep="")
        print(str("Ingrese el numero de alumnos:"), sep="")
        N = int(input())
    for X in range(1, N + 1):
        print(str("Ingrese la calificacion del alumno: "), str(X), sep="")
        NOTA = float(input())
        while NOTA <0  or  NOTA >10:
            print(str("La nota no puede ser negativa ni mayor a 10"), sep="")
            print(str("Ingrese la calificacion del alumno: "), str(X), sep="")
            NOTA = float(input())
        if NOTA >= 7:
            A = A + 1
        else:
            R = R + 1
    print(str("Cantidad de aprobados: "), str(A), sep="")
    print(str("Cantidad de reprobados: "), str(R), sep="")

if __name__ == "__main__":
    main()
