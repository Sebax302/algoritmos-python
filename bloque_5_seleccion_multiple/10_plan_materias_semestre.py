# Plan de materias según semestre

def main():
    S = 0
    M = 0
    P = 0.0

    # Ejercicio: Plan de materias según semestre
    print(str("Semestre actual (1 a 4):"), sep="")
    S = int(input())
    print(str("Promedio (0 a 10):"), sep="")
    P = float(input())
    if P < 0  or  P > 10  or  S < 1  or  S > 4:
        print(str("Datos invalidos"), sep="")
    else:
        # Materias base segun semestre
        match S:
            case 1 | 2:
                M = 5
            case 3 | 4:
                M = 4
        # Ajuste por promedio y limites del plan
        if P >= 8.5:
            M = M + 1
        else:
            if P < 7:
                M = M - 1
        if M < 3:
            M = 3
        if M > 6:
            M = 6
        print(str("Materias recomendadas: "), str(M), sep="")

if __name__ == "__main__":
    main()
