# Medios de transporte en Loja

def main():
    O = 0
    T = 0
    C = ""

    # Ejercicio: Medios de transporte en Loja
    # Tiempos referenciales para 5 km; varian con trafico y terreno
    print(str("1. Bus urbano"), sep="")
    print(str("2. Taxi"), sep="")
    print(str("3. Bicicleta"), sep="")
    print(str("4. Caminar"), sep="")
    O = int(input())
    match O:
        case 1:
            T = 30
            C = "Economico, depende de las paradas"
        case 2:
            T = 15
            C = "Comodo, sujeto al trafico"
        case 3:
            T = 25
            C = "Activo y sin combustible"
        case 4:
            T = 60
            C = "Saludable, requiere mas tiempo"
        case _:
            T = -1
            C = "Opcion no valida"
    if T >= 0:
        print(str("Tiempo aproximado: "), str(T), str(" minutos"), sep="")
    print(str(C), sep="")

if __name__ == "__main__":
    main()
