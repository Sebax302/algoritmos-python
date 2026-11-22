# Clasificación por rendimiento y asistencia

def main():
    P = 0.0
    A = 0.0
    CAT = ""

    # Ejercicio: Clasificación por rendimiento y asistencia
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el promedio (0 a 10):"), sep="")
    P = float(input())
    print(str("Ingrese la asistencia (0 a 100):"), sep="")
    A = float(input())
    # Proceso y cálculos
    if P < 0  or  P > 10  or  A < 0  or  A > 100:
        CAT = "Datos no validos"
    else:
        if P >= 9  and  A >= 90:
            CAT = "Excelente"
        else:
            if P >= 7  and  A >= 80:
                CAT = "Bueno"
            else:
                if P >= 6  and  A >= 70:
                    CAT = "Regular"
                else:
                    CAT = "Deficiente"
    print(str("Categoria: "), str(CAT), sep="")

if __name__ == "__main__":
    main()
