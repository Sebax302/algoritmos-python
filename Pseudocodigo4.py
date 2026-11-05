
# Declaraciones
compra = float(input("Ingrese el monto de la compra: "))

# Cuerpo
if compra >= 200:
    descuento = compra * 0.15
else:
    if compra >= 100:
        descuento = compra * 0.10
    else:
        descuento = compra * 0.05

total = compra - descuento

print("El descuento aplicado es:", descuento)
print("El monto a pagar es:", total)
