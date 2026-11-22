# Área de un triangulo

def main():
    B = 0.0
    H = 0.0
    A = 0.0

    # Ejercicio: Área de un triangulo
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingresar la base:"), sep="")
    B = float(input())
    print(str("Ingresar la altura:"), sep="")
    H = float(input())
    # Proceso y cálculos
    A = (B*H)/2
    print(str("La area del triangulo es:"), str(A), sep="")

if __name__ == "__main__":
    main()
