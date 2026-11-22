# Tarifa de parqueadero de estudiantes

def main():
    H = 0.0
    T = 0.0
    E = ""

    # Ejercicio: Tarifa de parqueadero de estudiantes
    # Datos
    print(str("Horas de permanencia:"), sep="")
    H = float(input())
    print(str("Es estudiante UTPL? (S/N):"), sep="")
    E = input().strip()
    if H < 0  or  (E != "S"  and  E != "N"):
        print(str("Datos invalidos"), sep="")
    else:
        # Tarifa base: un dolar por hora
        T = H * 1
        if E == "S":
            T = T * 0.50
            if H > 4:
                T = T * 1.20
        else:
            if H > 6:
                T = T * 1.20
        print(str("Total a pagar: $"), str(T), sep="")

if __name__ == "__main__":
    main()
