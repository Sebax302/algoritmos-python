# Conversión de base decimal a binario (método manual)
import math

def concat(a, b):
    return str(a) + str(b)

def main():
    NUM = 0
    RES = 0
    BIN = ""

    # Ejercicio: Conversión de base decimal a binario (método manual)
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese un numero entero decimal no negativo:"), sep="")
    NUM = int(input())
    # Proceso y cálculos
    while NUM < 0:
        print(str("El numero debe ser no negativo"), sep="")
        print(str("Ingrese un numero entero decimal no negativo:"), sep="")
        NUM = int(input())
    BIN = ""
    if NUM == 0:
        BIN = "0"
    else:
        while NUM > 0:
            RES = NUM % 2
            BIN = concat(str(RES), BIN)
            NUM = math.trunc(NUM / 2)
    print(str("Representacion binaria: "), str(BIN), sep="")

if __name__ == "__main__":
    main()
