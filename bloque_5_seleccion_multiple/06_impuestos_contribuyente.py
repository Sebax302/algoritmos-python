# Impuestos por tipo de contribuyente

def main():
    O = 0
    I = 0.0
    T = 0.0
    V = False

    # Ejercicio: Impuestos por tipo de contribuyente
    # Datos de ingreso anual
    print(str("Tipo: 1 Estudiante, 2 Independiente, 3 Empleado, 4 Empresa"), sep="")
    O = int(input())
    print(str("Ingreso anual:"), sep="")
    I = float(input())
    V = True
    T = 0
    if I < 0:
        print(str("Ingreso no valido"), sep="")
    else:
        # Impuesto por categoria, incluyendo recargo si procede
        match O:
            case 1:
                if I >= 5000:
                    T = I * 0.05
            case 2:
                T = I * 0.10
            case 3:
                T = I * 0.12
                if I > 20000:
                    T = T + I * 0.02
            case 4:
                T = I * 0.15
            case _:
                V = False
        if V:
            print(str("Impuesto anual: $"), str(T), sep="")
        else:
            print(str("Tipo invalido"), sep="")

if __name__ == "__main__":
    main()
