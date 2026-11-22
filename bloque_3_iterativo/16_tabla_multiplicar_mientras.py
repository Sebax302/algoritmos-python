# Tabla de multiplicacion con mientras

def main():
    K = 0
    I = 0
    R = 0

    # Ejercicio: Tabla de multiplicacion con mientras
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el numero entero para mostrar su tabla:"), sep="")
    K = int(input())
    # Proceso y cálculos
    I = 1
    while I <= 10:
        R = K * I
        print(str(K), str(" x "), str(I), str(" == "), str(R), sep="")
        I = I + 1

if __name__ == "__main__":
    main()
