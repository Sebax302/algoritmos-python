# Promedio final

def main():
    N1 = 0.0
    N2 = 0.0
    N3 = 0.0
    P = 0.0

    # Ejercicio: Promedio final
    # Variables y datos del problema
    # Ingreso y verificacion de la nota uno
    # Entrada de datos y validaciones
    print(str("Ingrese nota parcial 1"), sep="")
    N1 = float(input())
    # Proceso y cálculos
    while N1 < 0  or  N1 > 10:
        print(str("La nota no puede menor que 0 ni mayor a 10"), sep="")
        print(str("Ingrese nota parcial 1"), sep="")
        N1 = float(input())
    # Ingreso y verificacion de la nota dos
    print(str("Ingrese nota parcial 2"), sep="")
    N2 = float(input())
    while N2 < 0  or  N2 > 10:
        print(str("La nota no puede menor que 0 ni mayor a 10"), sep="")
        print(str("Ingrese nota parcial 2"), sep="")
        N2 = float(input())
    # Ingreso y verificacion de la nota tres
    print(str("Ingrese nota parcial 3"), sep="")
    N3 = float(input())
    while N3 < 0  or  N3 > 10:
        print(str("La nota no puede menor que 0 ni mayor a 10"), sep="")
        print(str("Ingrese nota parcial 3"), sep="")
        N3 = float(input())
    # Calculo del promedio
    P = (N1*0.30) + (N2*0.30) + (N3*0.40)
    if P >= 7:
        print(str("El estudiante aprueba y su promedio es:"), str(P), sep="")
    else:
        print(str("El estudiante no aprueba y su promedio es:"), str(P), sep="")

if __name__ == "__main__":
    main()
