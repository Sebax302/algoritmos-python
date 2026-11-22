# Ahorro con interés compuesto mensual

def main():
    CAP = 0.0
    DEP = 0.0
    TASA = 0.0
    SAL = 0.0
    N = 0
    MES = 0

    # Ejercicio: Ahorro con interés compuesto mensual
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el capital inicial:"), sep="")
    CAP = float(input())
    # Proceso y cálculos
    while CAP < 0:
        print(str("El capital no puede ser negativo"), sep="")
        print(str("Ingrese el capital inicial:"), sep="")
        CAP = float(input())
    print(str("Ingrese el deposito mensual:"), sep="")
    DEP = float(input())
    while DEP < 0:
        print(str("El deposito no puede ser negativo"), sep="")
        print(str("Ingrese el deposito mensual:"), sep="")
        DEP = float(input())
    print(str("Ingrese el numero de meses:"), sep="")
    N = int(input())
    while N <= 0:
        print(str("El numero de meses debe ser mayor que 0"), sep="")
        print(str("Ingrese el numero de meses:"), sep="")
        N = int(input())
    print(str("Ingrese la tasa mensual de interes (%):"), sep="")
    TASA = float(input())
    while TASA < 0:
        print(str("La tasa no puede ser negativa"), sep="")
        print(str("Ingrese la tasa mensual de interes (%):"), sep="")
        TASA = float(input())
    SAL = CAP
    for MES in range(1, N + 1):
        SAL = SAL + DEP
        SAL = SAL * (1 + TASA / 100)
        print(str("Saldo al finalizar el mes "), str(MES), str(": $"), str(SAL), sep="")
    print(str("Saldo final: $"), str(SAL), sep="")

if __name__ == "__main__":
    main()
