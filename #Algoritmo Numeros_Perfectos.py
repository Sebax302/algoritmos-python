#Algoritmo Numeros_Perfectos
n = int(input("Ingrese el número: "))

suma_divisores = 0

for divisor in range(1, n // 2 + 1):
    if n % divisor == 0:
        suma_divisores += divisor

if n > 0 and suma_divisores == n:
    print("El número es perfecto.")
else:
    print("El número no es perfecto.")