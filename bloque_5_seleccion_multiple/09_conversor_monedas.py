# Conversor de monedas con comisión

def main():
    O = 0
    M = 0.0
    T = 0.0
    C = 0.0
    CU = 0.0
    CD = 0.0
    R = 0.0

    # Ejercicio: Conversor de monedas con comisión
    # Tasas didacticas de la diapositiva, NO cotizaciones actuales
    print(str("Moneda: 1 EUR, 2 GBP, 3 JPY, 4 MXN"), sep="")
    O = int(input())
    print(str("Monto en USD:"), sep="")
    M = float(input())
    if M < 0  or  O < 1  or  O > 4:
        print(str("Datos invalidos"), sep="")
    else:
        # Tasa y comision por tipo
        match O:
            case 1:
                T = 0.92
                C = 0.01
            case 2:
                T = 0.78
                C = 0.01
            case 3:
                T = 149
                C = 0.015
            case 4:
                T = 17.2
                C = 0.02
        CU = M * C
        CD = CU * T
        R = M * T - CD
        print(str("Comision en USD: $"), str(CU), sep="")
        print(str("Comision en moneda destino: "), str(CD), sep="")
        print(str("Monto convertido neto: "), str(R), sep="")

if __name__ == "__main__":
    main()
