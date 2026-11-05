#Algoritmo Inversion_numero
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero //= 10

    print(f"El número invertido es: {invertido}")