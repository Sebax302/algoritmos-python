# Acceso a laboratorio de cómputo

def main():
    E = ""
    C = ""
    A = ""

    # Ejercicio: Acceso a laboratorio de cómputo
    # Datos de estudiante, carne y autorizacion
    print(str("Es estudiante? (S/N):"), sep="")
    E = input().strip()
    print(str("Tiene carne vigente? (S/N):"), sep="")
    C = input().strip()
    print(str("Tiene autorizacion especial? (S/N):"), sep="")
    A = input().strip()
    if (E != "S"  and  E != "N")  or  (C != "S"  and  C != "N")  or  (A != "S"  and  A != "N"):
        print(str("Responda en mayusculas S o N"), sep="")
    else:
        # Prioridad: estudiante con carne, o visitante autorizado
        if E == "S":
            if C == "S":
                print(str("Acceso permitido"), sep="")
            else:
                print(str("Acceso denegado: carne no vigente"), sep="")
        else:
            if A == "S":
                print(str("Ingreso temporal autorizado"), sep="")
            else:
                print(str("Acceso denegado"), sep="")

if __name__ == "__main__":
    main()
