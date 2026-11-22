# Conversión de coordenadas polares a cartesianas
import math

def main():
    R = 0.0
    G = 0.0
    RAD = 0.0
    X = 0.0
    Y = 0.0

    # Ejercicio: Conversión de coordenadas polares a cartesianas
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese el radio:"), sep="")
    R = float(input())
    print(str("Ingrese el angulo en grados:"), sep="")
    G = float(input())
    # Proceso y cálculos
    RAD = G * 3.14159265 / 180
    X = R * math.cos(RAD)
    Y = R * math.sin(RAD)
    print(str("Coordenada X: "), str(X), sep="")
    print(str("Coordenada Y: "), str(Y), sep="")

if __name__ == "__main__":
    main()
