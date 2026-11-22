# Determinación de estación del año

def main():
    MES = 0
    DIA = 0
    DM = 0
    EST = ""

    # Ejercicio: Determinación de estación del año
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el mes (1 a 12):"), sep="")
    MES = int(input())
    print(str("Ingrese el dia:"), sep="")
    DIA = int(input())
    # Proceso y cálculos
    DM = 31
    if MES == 4  or  MES == 6  or  MES == 9  or  MES == 11:
        DM = 30
    else:
        if MES == 2:
            DM = 28
    if MES < 1  or  MES > 12  or  DIA < 1  or  DIA > DM:
        print(str("Fecha no valida"), sep="")
    else:
        if (MES == 12  and  DIA >= 21)  or  MES == 1  or  MES == 2  or  (MES == 3  and  DIA <= 20):
            EST = "Verano"
        else:
            if (MES == 3  and  DIA >= 21)  or  MES == 4  or  MES == 5  or  (MES == 6  and  DIA <= 20):
                EST = "Otono"
            else:
                if (MES == 6  and  DIA >= 21)  or  MES == 7  or  MES == 8  or  (MES == 9  and  DIA <= 22):
                    EST = "Invierno"
                else:
                    EST = "Primavera"
        print(str("La estacion del anio es: "), str(EST), sep="")

if __name__ == "__main__":
    main()
