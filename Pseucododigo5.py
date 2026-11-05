
# Declaraciones
# Control de la n1
n1 = float(input("Ingrese la nota 1, entre 0 y 10: "))

while n1 < 0 or n1 > 10:
    print("Nota invalida")
    n1 = float(input("Ingrese la nota con los valores entre 0 y 10: "))

# Control de la n2
n2 = float(input("Ingrese la nota 2, entre 0 y 10: "))

while n2 < 0 or n2 > 10:
    print("Nota invalida")
    n2 = float(input("Ingrese la nota con los valores entre 0 y 10: "))

# Control de la n3
n3 = float(input("Ingrese la nota 3, entre 0 y 10: "))

while n3 < 0 or n3 > 10:
    print("Nota invalida")
    n3 = float(input("Ingrese la nota con los valores entre 0 y 10: "))

# Calculo del promedio
prom = (n1 + n2 + n3) / 3

print("El promedio es:", prom)
