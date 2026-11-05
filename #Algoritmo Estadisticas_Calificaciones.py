#Algoritmo Estadisticas_Calificaciones
n = int(input("Ingrese la cantidad de calificaciones: "))

while n <= 0:
    print("La cantidad debe ser mayor que cero.")
    n = int(input("Ingrese la cantidad de calificaciones: "))

suma = 0
aprobados = 0
reprobados = 0
mayor = None
menor = None

for i in range(1, n + 1):
    nota = float(input(f"Ingrese la calificación {i}: "))
    suma += nota

    if mayor is None or nota > mayor:
        mayor = nota
    if menor is None or nota < menor:
        menor = nota

    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1

promedio = suma / n

print(f"El promedio es: {promedio:.2f}")
print(f"La calificación mayor es: {mayor}")
print(f"La calificación menor es: {menor}")
print(f"La cantidad de aprobados es: {aprobados}")
print(f"La cantidad de reprobados es: {reprobados}")