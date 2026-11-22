# Máximo común divisor (Euclides)

def main():
    A = 0
    B = 0
    RES = 0

    # Ejercicio: Máximo común divisor (Euclides)
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el primer numero entero positivo:"), sep="")
    A = int(input())
    # Proceso y cálculos
    while A <= 0:
        print(str("El numero debe ser mayor que 0"), sep="")
        print(str("Ingrese el primer numero entero positivo:"), sep="")
        A = int(input())
    print(str("Ingrese el segundo numero entero positivo:"), sep="")
    B = int(input())
    while B <= 0:
        print(str("El numero debe ser mayor que 0"), sep="")
        print(str("Ingrese el segundo numero entero positivo:"), sep="")
        B = int(input())
    while B != 0:
        RES = A % B
        A = B
        B = RES
    print(str("El maximo comun divisor es: "), str(A), sep="")

if __name__ == "__main__":
    main()
