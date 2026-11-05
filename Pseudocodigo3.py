
# Algoritmo PromedioFinalUTPL_LOJA

# Declaraciones
# Control de ingreso de nota1
print("Ingrese la nota del primer parcial (0 a 10)")
nota1 = float(input())

while nota1 < 0 or nota1 > 10:
    print("Nota invalida. Debe estar entre 0 y 10")
    print("Ingrese nuevamente la nota del primer parcial")
    nota1 = float(input())

# Control de ingreso de nota2
print("Ingrese la nota del segundo parcial (0 a 10)")
nota2 = float(input())

while nota2 < 0 or nota2 > 10:
    print("Nota invalida. Debe estar entre 0 y 10")
    print("Ingrese nuevamente la nota del segundo parcial")
    nota2 = float(input())

# Control de ingreso de nota3
print("Ingrese la nota del tercer parcial (0 a 10)")
nota3 = float(input())

while nota3 < 0 or nota3 > 10:
    print("Nota invalida. Debe estar entre 0 y 10")
    print("Ingrese nuevamente la nota del tercer parcial")
    nota3 = float(input())

# Calculo del promedio ponderado
promedio = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)

print("El promedio final es:", promedio)

# Control de aprobacion
if promedio >= 7:
    print("El estudiante aprueba la asignatura")
else:
    print("El estudiante no aprueba la asignatura")
