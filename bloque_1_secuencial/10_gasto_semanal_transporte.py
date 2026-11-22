# Gasto semanal transporte

def main():
    VD = 0
    DS = 0
    PC = 0.0
    GS = 0.0

    # Ejercicio: Gasto semanal transporte
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el numero de viajes por dia:"), sep="")
    VD = int(input())
    # Proceso y cálculos
    while VD <= 0:
        print(str("Los viajes por dia deben ser mayores que 0"), sep="")
        print(str("Ingrese el numero de viajes por dia:"), sep="")
        VD = int(input())
    print(str("Ingrese el costo de cada pasaje:"), sep="")
    PC = float(input())
    while PC <= 0:
        print(str("El costo del pasaje debe ser mayor que 0"), sep="")
        print(str("Ingrese el costo de cada pasaje:"), sep="")
        PC = float(input())
    print(str("Ingrese los dias que viaja a la semana (1 a 7):"), sep="")
    DS = int(input())
    while DS < 1  or  DS > 7:
        print(str("Los dias deben estar entre 1 y 7"), sep="")
        print(str("Ingrese los dias que viaja a la semana (1 a 7):"), sep="")
        DS = int(input())
    GS = VD * PC * DS
    print(str("El gasto semanal de transporte es: $"), str(GS), sep="")

if __name__ == "__main__":
    main()
