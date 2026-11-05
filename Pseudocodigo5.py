
# Algoritmo Incremento_Salarial

# Declaraciones
salario = 1500
anio = 0

# Cuerpo
for anio in range(1, 7):
    salario = salario * 1.10
    print("Salario del año", anio, ":", round(salario, 2))

print("Salario final después de 6 años:", round(salario, 2))
