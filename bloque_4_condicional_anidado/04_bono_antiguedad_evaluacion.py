# Bono por antigüedad y evaluación

def main():
    A = 0.0
    S = 0.0
    B = 0.0
    T = 0.0
    E = ""

    # Ejercicio: Bono por antigüedad y evaluación
    # Entradas
    print(str("Antiguedad del trabajador en anos:"), sep="")
    A = float(input())
    print(str("Sueldo base:"), sep="")
    S = float(input())
    print(str("Evaluacion excelente? (S/N):"), sep="")
    E = input().strip()
    if A < 0  or  S < 0  or  (E != "S"  and  E != "N"):
        print(str("Datos invalidos"), sep="")
    else:
        # Nota: el enunciado no otorga bono justo a los 2 anos
        B = 0
        if A > 2:
            B = S * 0.10
            if E == "S":
                B = B + S * 0.05
        else:
            if A < 2:
                if E == "S":
                    B = S * 0.05
        T = S + B
        print(str("Bono: $"), str(B), sep="")
        print(str("Sueldo total: $"), str(T), sep="")

if __name__ == "__main__":
    main()
