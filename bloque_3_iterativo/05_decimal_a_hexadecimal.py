# Conversión de decimal a hexadecimal
import math

def concat(a, b):
    return str(a) + str(b)

def main():
    NUM = 0
    RES = 0
    HEX = ""
    DIG = ""

    # Ejercicio: Conversión de decimal a hexadecimal
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese un numero entero decimal no negativo:"), sep="")
    NUM = int(input())
    # Proceso y cálculos
    while NUM < 0:
        print(str("El numero debe ser no negativo"), sep="")
        print(str("Ingrese un numero entero decimal no negativo:"), sep="")
        NUM = int(input())
    HEX = ""
    if NUM == 0:
        HEX = "0"
    else:
        while NUM > 0:
            RES = NUM % 16
            if RES < 10:
                DIG = str(RES)
            else:
                match RES:
                    case 10:
                        DIG = "A"
                    case 11:
                        DIG = "B"
                    case 12:
                        DIG = "C"
                    case 13:
                        DIG = "D"
                    case 14:
                        DIG = "E"
                    case 15:
                        DIG = "F"
            HEX = concat(DIG, HEX)
            NUM = math.trunc(NUM / 16)
    print(str("Representacion hexadecimal: "), str(HEX), sep="")

if __name__ == "__main__":
    main()
