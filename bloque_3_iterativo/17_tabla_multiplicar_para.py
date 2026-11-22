# Tabla de multiplicar con for

def main():
    K = 0
    I = 0
    R = 0

    # Ejercicio: Tabla de multiplicar con for
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el numero entero para mostrar su tabla:"), sep="")
    K = int(input())
    # Proceso y cálculos
    for I in range(1, 10 + 1):
        R = K * I
        print(str(K), str(" x "), str(I), str(" == "), str(R), sep="")

if __name__ == "__main__":
    main()
