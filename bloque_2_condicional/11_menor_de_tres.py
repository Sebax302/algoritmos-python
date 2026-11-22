# Menor de tres numeros

def main():
    N1 = 0.0
    N2 = 0.0
    N3 = 0.0
    MEN = 0.0

    # Ejercicio: Menor de tres numeros
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el primer numero:"), sep="")
    N1 = float(input())
    print(str("Ingrese el segundo numero:"), sep="")
    N2 = float(input())
    print(str("Ingrese el tercer numero:"), sep="")
    N3 = float(input())
    # Proceso y cálculos
    if N1 <= N2  and  N1 <= N3:
        MEN = N1
    else:
        if N2 <= N1  and  N2 <= N3:
            MEN = N2
        else:
            MEN = N3
    print(str("El menor de los tres numeros es: "), str(MEN), sep="")

if __name__ == "__main__":
    main()
