# Compra con descuento

def main():
    P = 0.0
    IVA = 0.0
    PIVA = 0.0
    PD = 0.0
    PCD = 0.0
    PF = 0.0

    # Ejercicio: Compra con descuento
    # Variables y datos del problema
    # Proceso y cálculos
    IVA = 0.15
    # Entrada de datos y validaciones
    print(str("Ingresar el valor del producto"), sep="")
    P = float(input())
    while P <= 0:
        print(str("El valor de producto no puede ser menor ni igual a 0"), sep="")
        print(str("Ingresar el valor del producto"), sep="")
        P = float(input())
    PD = P*0.20
    PCD = P-PD
    PIVA = PCD*IVA
    PF = PCD+PIVA
    print(str("Descuento aplicado"), str(PD), sep="")
    print(str("Precio con el descuento"), str(PCD), sep="")
    print(str("IVA aplicado"), str(PIVA), sep="")
    print(str("Precio final"), str(PF), sep="")

if __name__ == "__main__":
    main()
