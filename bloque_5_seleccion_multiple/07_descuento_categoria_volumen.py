# Descuentos por categoría y volumen

def main():
    O = 0
    C = 0
    P = 0.0
    D = 0.0
    T = 0.0

    # Ejercicio: Descuentos por categoría y volumen
    # Categoria, cantidad y precio unitario
    print(str("Categoria: 1 Electronica, 2 Ropa, 3 Alimentos, 4 Otros"), sep="")
    O = int(input())
    print(str("Cantidad:"), sep="")
    C = int(input())
    print(str("Precio unitario:"), sep="")
    P = float(input())
    if C <= 0  or  P < 0  or  O < 1  or  O > 4:
        print(str("Datos invalidos"), sep="")
    else:
        # Descuento segun categoria y volumen
        D = 0
        match O:
            case 1:
                if C >= 10:
                    D = 0.05
            case 2:
                if C >= 5:
                    D = 0.10
            case 3:
                D = 0.03
            case 4:
                D = 0
        T = P * C * (1 - D)
        if T > 100:
            T = T * 0.98
        print(str("Total a pagar: $"), str(T), sep="")

if __name__ == "__main__":
    main()
