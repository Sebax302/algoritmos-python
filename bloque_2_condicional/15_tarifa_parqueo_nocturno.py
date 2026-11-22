# Tarifa de estacionamiento con recargo nocturno

def main():
    H = 0.0
    TB = 0.0
    T = 0.0
    N = ""

    # Ejercicio: Tarifa de estacionamiento con recargo nocturno
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese las horas de estacionamiento:"), sep="")
    H = float(input())
    print(str("Es horario nocturno? (S/N):"), sep="")
    N = input().strip()
    # Proceso y cálculos
    if H < 0  or  (N != "S"  and  N != "s"  and  N != "N"  and  N != "n"):
        print(str("Datos no validos"), sep="")
    else:
        TB = H * 1.50
        T = TB
        if H > 8:
            T = T * 1.25
        if N == "S"  or  N == "s":
            T = T * 1.30
        print(str("Tarifa base: $"), str(TB), sep="")
        print(str("Total a pagar: $"), str(T), sep="")

if __name__ == "__main__":
    main()
