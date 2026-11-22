# Calcular la longitud y el area de una circuferencia

def main():
    R = 0.0
    L = 0.0
    A = 0.0

    # Ejercicio: Calcular la longitud y el area de una circuferencia
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingresar el radio:"), sep="")
    R = float(input())
    # Proceso y cálculos
    L = 2*3.14159265*R
    A = 3.14159265*(R)**2
    print(str("La longitud es:"), str(L), sep="")
    print(str("El area del circulo es:"), str(A), sep="")

if __name__ == "__main__":
    main()
