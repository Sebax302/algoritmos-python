#Algoritmo Suma_serie_armonica
n = int(input("Ingrese N: "))

suma = 0.0

for i in range(1, n + 1):
    suma += 1 / i

print(f"La suma de la serie es: {suma:.4f}")