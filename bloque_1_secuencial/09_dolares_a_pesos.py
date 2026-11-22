# Conversión de dólares a pesos mexicanos

def main():
    D = 0.0
    C = 0.0
    P = 0.0

    # Ejercicio: Conversión de dólares a pesos mexicanos
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese la cantidad en dolares:"), sep="")
    D = float(input())
    # Proceso y cálculos
    while D < 0:
        print(str("La cantidad no puede ser negativa"), sep="")
        print(str("Ingrese la cantidad en dolares:"), sep="")
        D = float(input())
    print(str("Ingrese el valor de pesos por dolar:"), sep="")
    C = float(input())
    while C <= 0:
        print(str("El tipo de cambio debe ser mayor que 0"), sep="")
        print(str("Ingrese el valor de pesos por dolar:"), sep="")
        C = float(input())
    P = D * C
    print(str("La cantidad equivalente en pesos mexicanos es: "), str(P), sep="")

if __name__ == "__main__":
    main()
