# Descuento segun el tipo de cliente

def main():
    C = 0
    M = 0.0
    D = 0.0
    F = 0.0

    # Caso adicional 1: Descuento segun el tipo de cliente
    print(str("Tipo de cliente (1 == Estudiante, 2 == Empleado, 3 == General):"), sep="")
    C = int(input())
    print(str("Ingrese el monto de compra:"), sep="")
    M = float(input())
    # Se acepta solamente un tipo valido y un monto positivo
    if C >= 1  and  C <= 3  and  M > 0:
        # Descuento base mediante seleccion anidada
        if C == 1:
            D = 0.15
        else:
            if C == 2:
                D = 0.10
            else:
                D = 0
        # Descuento adicional sobre el porcentaje inicial
        if M > 50:
            D = D + 0.05
        F = M * (1 - D)
        print(str("Descuento aplicado: "), str(D * 100), str("%"), sep="")
        print(str("Total a pagar: $"), str(F), sep="")
    else:
        print(str("Tipo de cliente o monto no valido"), sep="")

if __name__ == "__main__":
    main()
