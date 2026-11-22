# Nivel académico y recomendación

def main():
    P = 0.0
    R = 0
    N = 0

    # Ejercicio: Nivel académico y recomendación
    print(str("Promedio de 0 a 10:"), sep="")
    P = float(input())
    print(str("Materias reprobadas:"), sep="")
    R = int(input())
    if P < 0  or  P > 10  or  R < 0:
        print(str("Datos invalidos"), sep="")
    else:
        # Primero se determina el nivel
        N = 4
        if P >= 9  and  R == 0:
            N = 1
        else:
            if P >= 8  and  R <= 1:
                N = 2
            else:
                if P >= 7:
                    N = 3
        # Luego se presenta la recomendacion
        match N:
            case 1:
                print(str("Excelente - Continua asi"), sep="")
            case 2:
                print(str("Bueno - Refuerza debilidades"), sep="")
            case 3:
                print(str("Regular - Necesitas mas estudio"), sep="")
            case 4:
                print(str("En riesgo - Busca tutoria"), sep="")

if __name__ == "__main__":
    main()
