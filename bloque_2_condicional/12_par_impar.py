# Par o Impar

def main():
    N = 0

    # Ejercicio: Par o Impar
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese un numero entero:"), sep="")
    N = int(input())
    # Proceso y cálculos
    if N % 2 == 0:
        print(str("El numero es PAR"), sep="")
    else:
        print(str("El numero es IMPAR"), sep="")

if __name__ == "__main__":
    main()
