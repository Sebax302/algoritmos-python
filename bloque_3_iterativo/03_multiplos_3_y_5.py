# Contar y sumar múltiplos de 3 y 5

def main():
    N = 0
    I = 0
    C = 0
    S = 0

    # Ejercicio: Contar y sumar múltiplos de 3 y 5
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese N:"), sep="")
    N = int(input())
    # Proceso y cálculos
    C = 0
    S = 0
    for I in range(1, N + 1):
        if I % 3 == 0  or  I % 5 == 0:
            C = C + 1
            S = S + I
    print(str("Cantidad de multiplos: "), str(C), sep="")
    print(str("Suma de multiplos: "), str(S), sep="")

if __name__ == "__main__":
    main()
