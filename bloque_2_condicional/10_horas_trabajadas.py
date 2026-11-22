# Horas de trabajo

def main():
    H = 0.0
    HE = 0.0
    SXH = 0.0
    S1 = 0.0
    S2 = 0.0
    SF = 0.0

    # Ejercicio: Horas de trabajo
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese las horas trabajadas"), sep="")
    H = float(input())
    print(str("Ingrese el sueldo por hora trabajada"), sep="")
    SXH = float(input())
    # Proceso y cálculos
    HE = 0
    # Horas trabajadas
    while H <= 0  or  H > 168:
        print(str("El numero ingresado debe ser mayor que 0 y menor o igual a 168 horas"), sep="")
        print(str("Ingrese las horas trabajadas"), sep="")
        H = float(input())
    # Sueldo por hora
    while SXH <= 0:
        print(str("El sueldo por hora debe ser mayor que 0"), sep="")
        print(str("Ingrese el sueldo por hora trabajada"), sep="")
        SXH = float(input())
    # Horas extras
    if H <= 40:
        SF = H * SXH
    else:
        HE = H - 40
        S1 = 40 * SXH
        S2 = HE * (SXH * 2)
        SF = S1 + S2
    print(str("Las horas extras trabajadas son: "), str(HE), sep="")
    print(str("El sueldo semanal es: "), str(SF), sep="")

if __name__ == "__main__":
    main()
