# Sistema de tarifas de taxi

def main():
    KM = 0.0
    TAR = 0.0
    TOT = 0.0
    NOC = ""

    # Ejercicio: Sistema de tarifas de taxi
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese la distancia del viaje en km:"), sep="")
    KM = float(input())
    # Proceso y cálculos
    while KM < 0:
        print(str("La distancia no puede ser negativa"), sep="")
        print(str("Ingrese la distancia del viaje en km:"), sep="")
        KM = float(input())
    print(str("Es de noche? Ingrese S o N:"), sep="")
    NOC = input().strip()
    while NOC != "S"  and  NOC != "N":
        print(str("Debe ingresar S o N"), sep="")
        print(str("Es de noche? Ingrese S o N:"), sep="")
        NOC = input().strip()
    TAR = 2 + (1.5 * KM)
    TOT = TAR
    if KM > 10:
        TOT = TOT + (TOT * 0.20)
    if NOC == "S":
        TOT = TOT + (TOT * 0.30)
    print(str("Total a pagar: $"), str(TOT), sep="")

if __name__ == "__main__":
    main()
