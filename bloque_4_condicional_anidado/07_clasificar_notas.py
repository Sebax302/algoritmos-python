# Clasificacion de notas con seleccion anidada

def main():
    N = 0.0

    # Ejemplo: Clasificacion de notas con seleccion anidada
    print(str("Ingrese la nota (0 a 10):"), sep="")
    N = float(input())
    # Primero comprobar el rango permitido
    if N >= 0  and  N <= 10:
        if N >= 9:
            print(str("Excelente"), sep="")
        else:
            if N >= 7:
                print(str("Aprobado"), sep="")
            else:
                print(str("Reprobado"), sep="")
    else:
        print(str("Nota fuera de rango"), sep="")

if __name__ == "__main__":
    main()
