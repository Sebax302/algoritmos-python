#Algoritmo Cuota_prestamo_interes_simple
capital = float(input("Ingrese el capital: "))
tasa = float(input("Ingrese la tasa anual en decimal (por ejemplo, 0.12 para 12%): "))
meses = int(input("Ingrese el número de meses: "))

if meses <= 0:
    print("El número de meses debe ser mayor que cero.")
else:
    interes = capital * tasa * (meses / 12)
    cuota = (capital + interes) / meses

    print(f"El interés total es: ${interes:.2f}")
    print(f"La cuota mensual es: ${cuota:.2f}")