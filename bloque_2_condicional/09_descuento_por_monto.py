# Descuento según monto de compra

def main():
    C = 0.0
    P = 0.0
    P1 = 0.0
    D = 0.0
    PF = 0.0

    # Ejercicio: Descuento según monto de compra
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el monto de la compra:"), sep="")
    C = float(input())
    # Proceso y cálculos
    while C < 0:
        print(str("El monto no puede ser negativo"), sep="")
        print(str("Ingrese el monto de la compra:"), sep="")
        C = float(input())
    if C >= 200:
        P = 0.15
    else:
        if C >= 100:
            P = 0.10
        else:
            P = 0.05
    D = C * P
    P1 = P * 100
    PF = C - D
    print(str("Descuento aplicado: "), str(P1), str("%"), sep="")
    print(str("Monto a pagar: $"), str(PF), sep="")

if __name__ == "__main__":
    main()
