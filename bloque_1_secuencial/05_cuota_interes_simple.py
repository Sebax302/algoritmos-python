# Cuota de préstamo con interés simple

def main():
    C = 0.0
    T = 0.0
    IT = 0.0
    CU = 0.0
    N = 0

    # Ejercicio: Cuota de préstamo con interés simple
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el capital:"), sep="")
    C = float(input())
    print(str("Ingrese la tasa anual en decimal:"), sep="")
    T = float(input())
    print(str("Ingrese el plazo en meses:"), sep="")
    N = int(input())
    # Proceso y cálculos
    if C < 0  or  T < 0  or  N <= 0:
        print(str("Datos no validos"), sep="")
    else:
        IT = C * T * (N / 12)
        CU = (C + IT) / N
        print(str("Interes total: $"), str(IT), sep="")
        print(str("Cuota mensual: $"), str(CU), sep="")

if __name__ == "__main__":
    main()
