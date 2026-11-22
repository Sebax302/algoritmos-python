# Día de la semana y tipo de actividad

def main():
    N = 0
    D = ""
    T = ""
    V = False

    # Ejercicio: Día de la semana y tipo de actividad
    print(str("Ingrese el dia (1 a 7):"), sep="")
    N = int(input())
    # Un dia se muestra una sola vez, con tipo de actividad
    V = True
    match N:
        case 1:
            D = "Lunes"
        case 2:
            D = "Martes"
        case 3:
            D = "Miercoles"
        case 4:
            D = "Jueves"
        case 5:
            D = "Viernes"
        case 6:
            D = "Sabado"
        case 7:
            D = "Domingo"
        case _:
            V = False
    if V:
        if N <= 5:
            T = "Dia de clases"
        else:
            T = "Fin de semana"
        print(str("Dia: "), str(D), sep="")
        print(str("Actividad: "), str(T), sep="")
    else:
        print(str("Numero de dia no valido"), sep="")

if __name__ == "__main__":
    main()
