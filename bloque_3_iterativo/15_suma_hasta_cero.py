# Suma de números hasta ingresar  0

def main():
    N = 0
    SUMA = 0

    # Ejercicio: Suma de números hasta ingresar  0
    # Variables y datos del problema
    # Proceso y cálculos
    SUMA = 0
    # Entrada de datos y validaciones
    print(str("Ingrese un numero (0 para terminar):"), sep="")
    N = int(input())
    while N != 0:
        SUMA = SUMA + (N)
        print(str("Ingrese un numero (0 para terminar):"), sep="")
        N = int(input())
    print(str("La suma total es: "), str(SUMA), sep="")

if __name__ == "__main__":
    main()
