# Conversor de unidades simple

def main():
    O = 0
    V = 0.0
    R = 0.0

    # Ejercicio: Conversor de unidades simple
    print(str("1. Km a m"), sep="")
    print(str("2. m a cm"), sep="")
    print(str("3. Horas a minutos"), sep="")
    print(str("4. Salir"), sep="")
    O = int(input())
    if O >= 1  and  O <= 3:
        print(str("Ingrese el valor a convertir:"), sep="")
        V = float(input())
        # Conversión por opción
        match O:
            case 1:
                R = V * 1000
            case 2:
                R = V * 100
            case 3:
                R = V * 60
        print(str("Resultado: "), str(R), sep="")
    else:
        match O:
            case 4:
                print(str("Fin del conversor"), sep="")
            case _:
                print(str("Opcion no valida"), sep="")

if __name__ == "__main__":
    main()
