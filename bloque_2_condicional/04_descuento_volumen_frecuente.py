# Descuento por volumen y cliente frecuente

def main():
    M = 0.0
    P = 0.0
    D = 0.0
    T = 0.0
    F = ""

    # Ejercicio: Descuento por volumen y cliente frecuente
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el monto de compra:"), sep="")
    M = float(input())
    print(str("Es cliente frecuente? (S/N):"), sep="")
    F = input().strip()
    # Proceso y cálculos
    if M < 0  or  (F != "S"  and  F != "s"  and  F != "N"  and  F != "n"):
        print(str("Datos no validos"), sep="")
    else:
        if M >= 500:
            P = 15
        else:
            if M >= 300:
                P = 10
            else:
                if M >= 100:
                    P = 5
                else:
                    P = 0
        if F == "S"  or  F == "s":
            P = P + 5
        D = M * P / 100
        T = M - D
        print(str("Porcentaje de descuento: "), str(P), str("%"), sep="")
        print(str("Descuento: $"), str(D), sep="")
        print(str("Total a pagar: $"), str(T), sep="")

if __name__ == "__main__":
    main()
