# Aprobación de asignatura

def main():
    P = 0.0

    # Ejercicio: Aprobación de asignatura
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el promedio final (0 a 10):"), sep="")
    P = float(input())
    # Proceso y cálculos
    while P < 0  or  P > 10:
        print(str("El promedio debe estar entre 0 y 10"), sep="")
        print(str("Ingrese el promedio final (0 a 10):"), sep="")
        P = float(input())
    if P >= 7:
        print(str("APRUEBA"), sep="")
    else:
        print(str("NO APRUEBA"), sep="")

if __name__ == "__main__":
    main()
