#Algoritmo Ahorro_Interes_Compuesto_Mensual
capital = float(input("Ingrese el capital inicial: "))
deposito = float(input("Ingrese el depósito mensual: "))
n_meses = int(input("Ingrese el número de meses: "))
tasa = float(input("Ingrese la tasa de interés (%): "))

saldo = capital

for mes in range(1, n_meses + 1):
    saldo += deposito
    saldo += saldo * tasa / 100
    print(f"El saldo del mes {mes} es: ${saldo:.2f}")