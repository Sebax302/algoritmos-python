# Clasificación de temperatura en Loja

def main():
    T = 0.0

    # Ejercicio: Clasificación de temperatura en Loja
    # Entrada
    print(str("Temperatura en grados Celsius:"), sep="")
    T = float(input())
    # Clasificación con selección anidada
    if T < 15:
        print(str("Clima frio"), sep="")
    else:
        if T <= 25:
            print(str("Clima templado"), sep="")
        else:
            print(str("Clima calido"), sep="")
            if T > 30:
                print(str("Alerta: calor extremo"), sep="")

if __name__ == "__main__":
    main()
