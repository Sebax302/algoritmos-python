#Algoritmo Vslor:Futuro_Anualidad
deposito_mensual = float(input("Ingrese el depósito mensual: "))
tasa_mensual = float(input("Ingrese la tasa mensual en decimal (por ejemplo, 0.02 para 2%): "))
n_meses = int(input("Ingrese el número de meses: "))

if deposito_mensual < 0 or tasa_mensual < 0 or n_meses <= 0:
    print("Ingrese depósitos y tasas no negativos, y un número de meses mayor que cero.")
else:
    total_depositado = deposito_mensual * n_meses

    if tasa_mensual == 0:
        valor_futuro = total_depositado
    else:
        valor_futuro = deposito_mensual * (
            ((1 + tasa_mensual) ** n_meses - 1) / tasa_mensual
        )

    print(f"El total depositado es: ${total_depositado:.2f}")
    print(f"El valor futuro es: ${valor_futuro:.2f}")