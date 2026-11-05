#Algoritmo Simulacion_ahorro
n = int(input("Ingrese el número de meses: "))

saldo = 0.0

for i in range(1, n + 1):
    aporte = float(input(f"Ingrese el aporte del mes {i}: "))
    saldo = (saldo + aporte) * 1.008

print(f"El saldo final es: ${saldo:.2f}")