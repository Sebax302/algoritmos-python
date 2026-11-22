# Diagnóstico 3 - Estadísticas de ventas hasta -1

def main():
    D = 0
    C = 0
    DM = 0
    V = 0.0
    S = 0.0
    P = 0.0
    MAX = 0.0

    # Ejercicio: Diagnóstico 3 - Estadísticas de ventas hasta -1
    # Acumuladores y control de dias validos
    S = 0
    D = 0
    C = 0
    DM = 0
    MAX = 0
    print(str("Venta diaria (-1 para terminar):"), sep="")
    V = float(input())
    # Las ventas negativas distintas de -1 no cuentan como dias
    while V != -1:
        if V < 0:
            print(str("Venta no valida; ingrese cero o un valor positivo"), sep="")
        else:
            D = D + 1
            S = S + V
            if V > 500:
                C = C + 1
            if D == 1  or  V > MAX:
                MAX = V
                DM = D
        print(str("Siguiente venta (-1 para terminar):"), sep="")
        V = float(input())
    # Resumen, evitando dividir por cero
    print(str("Total de ventas: $"), str(S), sep="")
    print(str("Dias con venta superior a $500: "), str(C), sep="")
    if D > 0:
        P = S / D
        print(str("Promedio de ventas: $"), str(P), sep="")
        print(str("Dia de mayor venta: "), str(DM), sep="")
        print(str("Mayor venta: $"), str(MAX), sep="")
    else:
        print(str("Promedio: no hay ventas registradas"), sep="")
        print(str("No hay dia con mayor venta"), sep="")

if __name__ == "__main__":
    main()
