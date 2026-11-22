# Diagnóstico 2 - Clasificación para beca

def main():
    P = 0.0
    R = 0
    B = 0
    C = ""

    # Ejercicio: Diagnóstico 2 - Clasificación para beca
    # Datos de postulacion
    print(str("Promedio (0 a 10):"), sep="")
    P = float(input())
    print(str("Materias reprobadas:"), sep="")
    R = int(input())
    print(str("Es de primer ciclo? (S/N):"), sep="")
    C = input().strip()
    if P < 0  or  P > 10  or  R < 0  or  (C != "S"  and  C != "N"):
        print(str("Datos invalidos"), sep="")
    else:
        # Se evalua de mayor a menor porcentaje de beca
        if P >= 9  and  R == 0  and  C == "S":
            B = 100
        else:
            if P >= 8  and  R <= 1:
                B = 70
            else:
                if P >= 7  and  R <= 2:
                    B = 40
                else:
                    B = 0
        print(str("Porcentaje de beca: "), str(B), str("%"), sep="")
        if B > 0:
            print(str("Beca aprobada"), sep="")
        else:
            print(str("Beca rechazada"), sep="")

if __name__ == "__main__":
    main()
