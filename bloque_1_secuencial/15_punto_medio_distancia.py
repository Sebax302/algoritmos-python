# Punto medio y distancia entre dos puntos
import math

def main():
    X1 = 0.0
    Y1 = 0.0
    X2 = 0.0
    Y2 = 0.0
    DIS = 0.0
    XM = 0.0
    YM = 0.0

    # Ejercicio: Punto medio y distancia entre dos puntos
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese la coordenada x del primer punto:"), sep="")
    X1 = float(input())
    print(str("Ingrese la coordenada y del primer punto:"), sep="")
    Y1 = float(input())
    print(str("Ingrese la coordenada x del segundo punto:"), sep="")
    X2 = float(input())
    print(str("Ingrese la coordenada y del segundo punto:"), sep="")
    Y2 = float(input())
    # Proceso y cálculos
    DIS = math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
    XM = (X1 + X2) / 2
    YM = (Y1 + Y2) / 2
    print(str("Distancia entre los puntos: "), str(DIS), sep="")
    print(str("Punto medio: ("), str(XM), str(", "), str(YM), str(")"), sep="")

if __name__ == "__main__":
    main()
