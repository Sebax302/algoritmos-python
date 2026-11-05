#Algoritmo_Maximo_Comun_Divisor
n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

n1 = abs(n1)
n2 = abs(n2)

while n2 != 0:
    n1, n2 = n2, n1 % n2

print(f"El máximo común divisor (MCD) es: {n1}")