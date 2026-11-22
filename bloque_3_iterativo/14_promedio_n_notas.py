# Promedio de N notas

def main():
    N = 0
    I = 0
    NOTA = 0.0
    SUMA = 0.0
    P = 0.0

    # Ejercicio: Promedio de N notas
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese la cantidad de notas:"), sep="")
    N = int(input())
    # Proceso y cálculos
    while N <= 0:
        print(str("La cantidad de notas debe ser mayor que 0"), sep="")
        print(str("Ingrese la cantidad de notas:"), sep="")
        N = int(input())
    SUMA = 0
    for I in range(1, N + 1):
        print(str("Ingrese la nota "), str(I), str(" (0 a 10):"), sep="")
        NOTA = float(input())
        while NOTA < 0  or  NOTA > 10:
            print(str("La nota debe estar entre 0 y 10"), sep="")
            print(str("Ingrese la nota "), str(I), str(" (0 a 10):"), sep="")
            NOTA = float(input())
        SUMA = SUMA + NOTA
    P = SUMA / N
    print(str("El promedio de las notas es: "), str(P), sep="")

if __name__ == "__main__":
    main()
