# Producto su suma y media Aritmetica

def main():
    N1 = 0.0
    N2 = 0.0
    N3 = 0.0
    N4 = 0.0
    S = 0.0
    P = 0.0
    M = 0.0

    # Ejercicio: Producto su suma y media Aritmetica
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el primer numero"), sep="")
    N1 = float(input())
    print(str("Ingrese el segundo numero"), sep="")
    N2 = float(input())
    print(str("Ingrese el trecer numero"), sep="")
    N3 = float(input())
    print(str("Ingrese el cuarto numero"), sep="")
    N4 = float(input())
    # Proceso y cálculos
    S = N1+N2+N3+N4
    P = N1*N2*N3*N4
    M = S/4
    print(str("La suma es:"), str(S), sep="")
    print(str("Es producto es:"), str(P), sep="")
    print(str("La media aritmetica es:"), str(M), sep="")

if __name__ == "__main__":
    main()
