#Algoritmo Cálculo_hipotenusa_área_triángulo_rectángulo
import math

cateto1 = float(input("Ingrese el primer cateto: "))
cateto2 = float(input("Ingrese el segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
area = (cateto1 * cateto2) / 2

print(f"La hipotenusa es: {hipotenusa:.2f}")
print(f"El área es: {area:.2f}")