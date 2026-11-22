# Menu de operaciones con control multiple

def main():
    O = 0

    # Ejemplo: Menu de operaciones con control multiple
    # Este menu solo identifica la operacion elegida, como solicita el ejemplo
    print(str("1. Sumar"), sep="")
    print(str("2. Restar"), sep="")
    print(str("3. Multiplicar"), sep="")
    print(str("4. Salir"), sep="")
    print(str("Elija una opcion:"), sep="")
    O = int(input())
    match O:
        case 1:
            print(str("Operacion: Suma"), sep="")
        case 2:
            print(str("Operacion: Resta"), sep="")
        case 3:
            print(str("Operacion: Multiplicacion"), sep="")
        case 4:
            print(str("Saliendo del programa"), sep="")
        case _:
            print(str("Opcion no valida"), sep="")

if __name__ == "__main__":
    main()
