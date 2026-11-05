#Algoritmo Conversion_coordenadas_polares
import math

radio = float(input("Ingrese el radio: "))
angulo = float(input("Ingrese el ángulo en grados: "))

radianes = math.radians(angulo)
x = radio * math.cos(radianes)
y = radio * math.sin(radianes)

print(f"La coordenada x es: {x:.2f}")
print(f"La coordenada y es: {y:.2f}")