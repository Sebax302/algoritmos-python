# Factorial de un numero

def main():
    N = 0
    X = 0
    F = 0

    # Ejercicio: Factorial de un numero
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese un numero entero"), sep="")
    N = int(input())
    # Proceso y cálculos
    if N < 0:
        print(str("No existe factorial para numeros negativos"), sep="")
    else:
        X = N
        F = 1
        while X>=1:
            F = F*X
            X = X-1
        print(str("El factorial del numero es:"), str(F), sep="")

if __name__ == "__main__":
    main()
