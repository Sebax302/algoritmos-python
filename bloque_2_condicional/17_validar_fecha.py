# Validación de fecha

def main():
    DIA = 0
    MES = 0
    ANIO = 0
    DM = 0
    BIS = False

    # Ejercicio: Validación de fecha
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el dia:"), sep="")
    DIA = int(input())
    print(str("Ingrese el mes:"), sep="")
    MES = int(input())
    print(str("Ingrese el anio:"), sep="")
    ANIO = int(input())
    # Proceso y cálculos
    DM = 0
    BIS = False
    if ANIO > 0  and  MES >= 1  and  MES <= 12  and  DIA >= 1:
        if ANIO % 400 == 0  or  (ANIO % 4 == 0  and  ANIO % 100 != 0):
            BIS = True
        if MES == 2:
            if BIS:
                DM = 29
            else:
                DM = 28
        else:
            if MES == 4  or  MES == 6  or  MES == 9  or  MES == 11:
                DM = 30
            else:
                DM = 31
    if DM > 0  and  DIA <= DM:
        print(str("La fecha es valida"), sep="")
    else:
        print(str("La fecha no es valida"), sep="")

if __name__ == "__main__":
    main()
