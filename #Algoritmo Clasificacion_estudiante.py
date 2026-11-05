#Algoritmo Clasificacion_estudiante
promedio = float(input("Ingrese el promedio: "))
asistencia = float(input("Ingrese el porcentaje de asistencia: "))

if promedio >= 9 and asistencia >= 90:
    categoria = "Excelente"
elif promedio >= 7 and asistencia >= 80:
    categoria = "Bueno"
elif promedio >= 6 and asistencia >= 70:
    categoria = "Regular"
else:
    categoria = "Deficiente"

print(f"La categoría es: {categoria}")