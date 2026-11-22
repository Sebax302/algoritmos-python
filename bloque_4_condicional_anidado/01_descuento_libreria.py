# Descuento en librería de Loja

def main():
    E = ""
    M = 0.0
    D = 0.0
    T = 0.0

    # Ejercicio: Descuento en librería de Loja
    # Entrada y validación
    print(str("Es estudiante UTPL? (S/N):"), sep="")
    E = input().strip()
    print(str("Monto de compra:"), sep="")
    M = float(input())
    if M < 0  or  (E != "S"  and  E != "N"  and  E != "s"  and  E != "n"):
        print(str("Datos invalidos"), sep="")
    else:
        # Descuentos por tipo de cliente
        D = 0
        if E == "S"  or  E == "s":
            D = 20
            if M > 30:
                D = D + 5
        else:
            if M > 50:
                D = 10
        T = M * (1 - D / 100)
        print(str("Descuento aplicado: "), str(D), str("%"), sep="")
        print(str("Total a pagar: $"), str(T), sep="")

if __name__ == "__main__":
    main()
