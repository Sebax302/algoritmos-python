#Algoritmo Multiplos_de_3_y_5
n = int(input("Ingrese N: "))

cantidad = 0
suma = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        cantidad += 1
        suma += i

print(f"La cantidad de múltiplos de 3 o 5 es: {cantidad}")
print(f"La suma de esos múltiplos es: {suma}")