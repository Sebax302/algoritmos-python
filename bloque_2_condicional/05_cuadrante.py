# Determinación de cuadrante

def main():
    X = 0.0
    Y = 0.0

    # Ejercicio: Determinación de cuadrante
    # Variables y datos del problema
    # Entrada de datos y validaciones
    print(str("Ingrese la coordenada X:"), sep="")
    X = float(input())
    print(str("Ingrese la coordenada Y:"), sep="")
    Y = float(input())
    # Proceso y cálculos
    if X == 0  and  Y == 0:
        print(str("El punto esta en el origen"), sep="")
    else:
        if X == 0:
            print(str("El punto esta sobre el eje Y"), sep="")
        else:
            if Y == 0:
                print(str("El punto esta sobre el eje X"), sep="")
            else:
                if X > 0  and  Y > 0:
                    print(str("Primer cuadrante"), sep="")
                else:
                    if X < 0  and  Y > 0:
                        print(str("Segundo cuadrante"), sep="")
                    else:
                        if X < 0  and  Y < 0:
                            print(str("Tercer cuadrante"), sep="")
                        else:
                            print(str("Cuarto cuadrante"), sep="")

if __name__ == "__main__":
    main()
