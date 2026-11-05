#Algoritmo Numero_Armstrong
numero = int(input("Ingrese un número de tres dígitos: "))

if 100 <= numero <= 999:
    original = numero
    suma = 0

    while numero > 0:
        digito = numero % 10
        suma += digito ** 3
        numero //= 10

    if suma == original:
        print("El número es Armstrong.")
    else:
        print("El número no es Armstrong.")
else:
    print("Debe ingresar un número de tres dígitos.")