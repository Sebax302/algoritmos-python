# Descuento de transporte urbano en Loja

def main():
    E = 0
    H = 0
    T = 0.0
    D = 0.0
    F = 0.0

    # Ejemplo: Descuento de transporte urbano en Loja
    # Ingreso de datos
    print(str("Es estudiante? (1 == Si, 0 == No):"), sep="")
    E = int(input())
    print(str("Ingrese la hora del viaje (0 a 23):"), sep="")
    H = int(input())
    print(str("Ingrese la tarifa base:"), sep="")
    T = float(input())
    # Verificar los datos antes de calcular
    if (E == 0  or  E == 1)  and  (H >= 0  and  H <= 23)  and  T >= 0:
        D = 0
        # Seleccion anidada por tipo de pasajero y horario
        if E == 1:
            D = 0.30
            if H >= 9  and  H <= 16:
                D = D + 0.10
        else:
            if H >= 9  and  H <= 16:
                D = 0.10
        F = T * (1 - D)
        print(str("Descuento aplicado: "), str(D * 100), str("%"), sep="")
        print(str("Tarifa final: $"), str(F), sep="")
    else:
        print(str("Datos no validos"), sep="")

if __name__ == "__main__":
    main()
