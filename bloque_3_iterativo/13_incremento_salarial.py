# Incremento salarial anual

def main():
    S = 0.0
    A = 0

    # Ejercicio: Incremento salarial anual
    # Variables y datos del problema
    # Proceso y cálculos
    S = 1500
    A = 1
    while A <= 6:
        S = S * 1.10
        # Entrada de datos y validaciones
        print(str("Salario al finalizar el año "), str(A), str(": $"), str(S), sep="")
        A = A + 1
    print(str("Salario final despues de 6 años: $"), str(S), sep="")

if __name__ == "__main__":
    main()
