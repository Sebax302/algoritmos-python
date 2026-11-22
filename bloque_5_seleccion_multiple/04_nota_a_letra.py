# Clasificación de notas por letra

def main():
    L = ""

    # Ejercicio: Clasificación de notas por letra
    print(str("Letra de calificacion (A, B, C, D, F):"), sep="")
    L = input().strip()
    L = str.upper(L)
    # Correspondencia entre letra y rango
    match L:
        case "A":
            print(str("Nota entre 9.0 y 10.0"), sep="")
        case "B":
            print(str("Nota entre 8.0 y 8.9"), sep="")
        case "C":
            print(str("Nota entre 7.0 y 7.9"), sep="")
        case "D":
            print(str("Nota entre 6.0 y 6.9"), sep="")
        case "F":
            print(str("Nota entre 0.0 y 5.9"), sep="")
        case _:
            print(str("Letra no valida"), sep="")

if __name__ == "__main__":
    main()
