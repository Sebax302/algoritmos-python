#Algoritmo Costo_envío_peso_volumétrico
peso_real = float(input("Ingrese el peso real (kg): "))
largo = float(input("Ingrese el largo (cm): "))
ancho = float(input("Ingrese el ancho (cm): "))
alto = float(input("Ingrese el alto (cm): "))

tarifa = 2.50
peso_volumetrico = (largo * ancho * alto) / 5000
peso_a_cobrar = max(peso_real, peso_volumetrico)
costo_total = peso_a_cobrar * tarifa

print(f"El peso volumétrico es: {peso_volumetrico:.2f} kg")
print(f"El peso a cobrar es: {peso_a_cobrar:.2f} kg")
print(f"El costo total es: ${costo_total:.2f}")