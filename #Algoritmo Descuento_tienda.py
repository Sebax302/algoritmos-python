#Algoritmo Descuento_tienda
monto = float(input("Ingrese el monto de compra: "))
frecuente = input("¿Es cliente frecuente? (S/N): ").strip().upper()

if monto >= 500:
    descuento = 0.15
elif monto >= 300:
    descuento = 0.10
elif monto >= 100:
    descuento = 0.05
else:
    descuento = 0

if frecuente == "S":
    descuento += 0.05

total = monto * (1 - descuento)

print(f"El descuento es: {descuento * 100:.0f}%")
print(f"El total a pagar es: ${total:.2f}")