# Menú de cafetería UTPL

def main():
    O = 0

    # Ejercicio: Menú de cafetería UTPL
    # Menú
    print(str("1. Cafe ($1.50)"), sep="")
    print(str("2. Jugo ($1.20)"), sep="")
    print(str("3. Sandwich ($2.50)"), sep="")
    print(str("4. Salir"), sep="")
    O = int(input())
    # Seleccion del producto
    match O:
        case 1:
            print(str("Cafe: $1.50"), sep="")
        case 2:
            print(str("Jugo: $1.20"), sep="")
        case 3:
            print(str("Sandwich: $2.50"), sep="")
        case 4:
            print(str("Gracias por visitar la cafeteria"), sep="")
        case _:
            print(str("Opcion no valida"), sep="")

if __name__ == "__main__":
    main()
