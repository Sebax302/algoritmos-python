# Clasificación de triángulo por ángulos

def main():
    A1 = 0.0
    A2 = 0.0
    A3 = 0.0
    SUMA = 0.0
    MAY = 0.0

    # Ejercicio: Clasificación de triángulo por ángulos
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el primer angulo:"), sep="")
    A1 = float(input())
    print(str("Ingrese el segundo angulo:"), sep="")
    A2 = float(input())
    print(str("Ingrese el tercer angulo:"), sep="")
    A3 = float(input())
    # Proceso y cálculos
    SUMA = A1 + A2 + A3
    if A1 <= 0  or  A2 <= 0  or  A3 <= 0  or  SUMA != 180:
        print(str("Error: los angulos no forman un triangulo"), sep="")
    else:
        MAY = A1
        if A2 > MAY:
            MAY = A2
        if A3 > MAY:
            MAY = A3
        if MAY < 90:
            print(str("El triangulo es acutangulo"), sep="")
        else:
            if MAY == 90:
                print(str("El triangulo es rectangulo"), sep="")
            else:
                print(str("El triangulo es obtusangulo"), sep="")

if __name__ == "__main__":
    main()
